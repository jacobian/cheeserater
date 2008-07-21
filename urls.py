import os
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.static import serve
from cheeserater.packages.views import homepage
from cheeserater.packages.models import Package
from voting.views import vote_on_object

urlpatterns = patterns('',
    (r'^accounts/',       include('cheeserater.accounts.urls')),
    (r'^admin/(.*)$',     admin.site.root),
    (r'^packages/',       include('cheeserater.packages.urls')),
    (
        r'^vote/package/(?P<object_id>.*?)/(?P<direction>up|down)/$', 
        vote_on_object, {
            "model": Package,
            "allow_xmlhttprequest": True,
        },
        "vote_on_package"
    ),
    (r'^$',               homepage),
)

if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^m/(?P<path>.*)$', serve, {
            'document_root' : os.path.join(os.path.dirname(__file__), "media")
        })
    )

admin.autodiscover()