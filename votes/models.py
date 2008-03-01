from django.db import models, connection
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.auth.models import User

class VoteManager(models.Manager):
    def get_score(self, obj):
        """
        Get the total score for ``obj``.
        """
        ctype = ContentType.objects.get_for_model(obj)
        cursor = connection.cursor()
        query = "SELECT SUM(vote) FROM votes WHERE content_type_id = %s AND object_pk = %s"
        cursor.execute(query, [ctype.id, obj._get_pk_val()])
        return cursor.fetchone()[0]
        
    def record_vote(self, obj, user, vote):
        """
        Record a user's vote (+/- 1) on a given object. Only allows a given user
        to vote once (though that vote may be changed).
        """
        if vote not in (+1, -1):
            raise ValueError("Invalid vote (must be +1/-1)")
        v, created = self.get_or_create(
            user         = user,
            content_type = ContentType.objects.get_for_model(obj),
            object_pk    = obj._get_pk_val(),
            defaults     = {"vote" : vote}
        )
        if not created:
            v.vote = vote
            v.save()
        return v
        
    def get_top(self, Model, limit=10, reversed=False):
        """
        Get the top N scored objects for a given model.
        
        Yields (object, score) tuples.
        """
        ctype = ContentType.objects.get_for_model(Model)
        query = "SELECT object_pk, SUM(vote) AS score FROM votes " \
                " WHERE content_type_id = %s " \
                " GROUP BY object_pk "
        if reversed:
            query += "HAVING SUM(vote) < 0 ORDER BY SUM(vote) ASC LIMIT %s"
        else:
            query += "HAVING SUM(vote) > 0 ORDER BY SUM(vote) DESC LIMIT %s"
        cursor = connection.cursor()
        cursor.execute(query, [ctype.id, limit])
        results = cursor.fetchall()
        
        # Use in_bulk() to avoid O(limit) db hits. .  
        objects = Model.objects.in_bulk([pk for pk, score in results])
        
        # Convert the PK keys into strings so that they match what's returned
        # by the object_pk field.
        objects = dict((str(k), v) for k, v in objects.iteritems())
        
        # Yield each object, score pair. Because of the lqzy nature
        # of generic relations, missing objects are silently ignored
        for pk, score in results:
            if pk in objects:
                yield objects[pk], score
                
    def get_bottom(self, Model, limit=10):
        """
        Get the bottom (i.e. must negative) N scored objects for a given model.
        
        Yields (object, score) tuples.
        """
        return self.get_top(Model, limit, True)

SCORES = [
    ("+1", +1),
    ("-1", -1),
]

class Vote(models.Model):
    user         = models.ForeignKey(User)
    content_type = models.ForeignKey(ContentType)
    object_pk    = models.TextField()
    object       = GenericForeignKey("content_type", "object_pk")
    vote         = models.SmallIntegerField(choices=SCORES)

    objects = VoteManager()

    class Meta:
        db_table = "votes"

    class Admin:
        pass

    def __str__(self):
        return "%s: %s on %s" % (self.user, self.vote, self.object)
