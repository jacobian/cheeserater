from django.conf.urls.defaults import *
from cheeserater.votes.views import vote

urlpatterns = patterns("",
    # This pattern might be a little too clever, but I like it
    (r'^(?P<ctype_id>\d+)/(?P<object_pk>.*?)/(?P<direction>up|down)/$', vote)
)