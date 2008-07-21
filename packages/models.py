import re
import urllib
from django.db import models

CHEESESHOP = "http://cheeseshop.python.org/pypi"

class Topic(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
        
    @models.permalink
    def permalink(self):
        return "cheeserater.packages.views.topic_detail", [self.slug]

class Category(models.Model):
    topic = models.ForeignKey(Topic, related_name="categories")
    value = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return "%s :: %s" % (self.topic.name, self.value)

    @models.permalink
    def permalink(self):
        return "cheeserater.packages.views.category_detail", [self.topic.slug, self.slug]

class Package(models.Model):
    name        = models.CharField(max_length=300)
    version     = models.CharField(max_length=300, blank=True)
    author      = models.CharField(max_length=300, blank=True)
    home_page   = models.URLField(blank=True)
    summary     = models.TextField()
    description = models.TextField(blank=True)
    keywords    = models.TextField(blank=True)
    categories  = models.ManyToManyField(Category, related_name="packages")

    class Meta:
        ordering = ["name"]
        verbose_name = "cheeseshop package"
        verbose_name_plural = "cheeseshop packages"

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
