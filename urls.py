import os
from django.conf import settings
from django.conf.urls.defaults import *
from django.views.static import serve
from cheeserater.packages.views import homepage

urlpatterns = patterns('',
    (r'^accounts/',       include('cheeserater.accounts.urls')),
    (r'^admin/',          include('django.contrib.admin.urls')),
    (r'^packages/',       include('cheeserater.packages.urls')),
    (r'^vote/',           include('cheeserater.votes.urls')),
    (r'^$',               homepage),
)

if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^m/(?P<path>.*)$', serve, {
            'document_root' : os.path.join(os.path.dirname(__file__), "media")
        })
    )
