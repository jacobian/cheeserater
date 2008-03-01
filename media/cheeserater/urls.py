from django.conf import settings
from django.conf.urls.defaults import *
from django.views.static import serve
from cheeserater.packages.views import homepage
from unipath import FSPath as Path

urlpatterns = patterns('',
    (r'^accounts/',       include('cheeserater.accounts.urls')),
    (r'^admin/',          include('django.contrib.admin.urls')),
    (r'^packages/',       include('cheeserater.packages.urls')),
    (r'^vote/',           include('cheeserater.votes.urls')),
    (r'^$',               homepage),
)

if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^m/(?P<path>.*)$', serve, {'document_root' : Path(__file__).parent.child("media")})
    )
