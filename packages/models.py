import re
import urllib
from django.db import models

CHEESESHOP = "http://cheeseshop.python.org/pypi"

class Topic(models.Model):
    name = models.CharField(maxlength=100)
    slug = models.SlugField(prepopulate_from=("name",))

    class Meta:
        ordering = ["name"]

    class Admin:
        list_display = ('name',)

    def __str__(self):
        return self.name
        
    @models.permalink
    def permalink(self):
        return "cheeserater.packages.views.topic_detail", [self.slug]

class Category(models.Model):
    topic = models.ForeignKey(Topic, related_name="categories")
    value = models.CharField(maxlength=100)
    slug = models.SlugField(prepopulate_from=("value",))

    class Meta:
        verbose_name_plural = "categories"

    class Admin:
        pass

    def __str__(self):
        return "%s :: %s" % (self.topic.name, self.value)

    @models.permalink
    def permalink(self):
        return "cheeserater.packages.views.category_detail", [self.topic.slug, self.slug]

class Package(models.Model):
    name        = models.CharField(maxlength=300)
    version     = models.CharField(maxlength=300, blank=True)
    author      = models.CharField(maxlength=300, blank=True)
    home_page   = models.URLField(blank=True)
    summary     = models.TextField()
    description = models.TextField(blank=True)
    keywords    = models.TextField(blank=True)
    categories  = models.ManyToManyField(Category, related_name="packages")

    class Meta:
        ordering = ["name"]

    class Admin:
        list_display = ('name', 'version', 'summary')
        search_fields = ('name', 'summary', 'keywords')

    def __str__(self):
        return self.name
        
    @models.permalink
    def permalink(self):
        return "cheeserater.packages.views.package_detail", [self.slug]

    @property
    def slug(self):
        return urllib.quote_plus(self.name)

    @property
    def pypi_link(self):
        return "%s/%s/%s/" % (CHEESESHOP, self.slug, self.version)
        
    @property
    def keyword_list(self):
        return sorted(re.split("[ ,]+", self.keywords), key=str.lower)
