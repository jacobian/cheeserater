from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from cheeserater.votes.models import Vote

@login_required
def vote(request, ctype_id, object_pk, direction):
    # Look up the object to vote on.
    try:
        ctype = ContentType.objects.get(pk=ctype_id)
        obj = ctype.get_object_for_this_type(pk=object_pk)
    except ObjectDoesNotExist:
        raise Http404
    
    # Convert the clever URL up/down into +1/-1 and record the vote
    v = {"up" : +1, "down": -1}[direction]
    Vote.objects.record_vote(obj, request.user, v)
    
    # Redirect to "next" or the object's permalink()
    next = request.REQUEST.get("next", obj.permalink())
    return HttpResponseRedirect(next)