from django.conf.urls.defaults import *
from cheeserater.accounts.views import register
from django.contrib.auth import views as authviews

urlpatterns = patterns('', 
    (r'^login/$',                authviews.login),
    (r'^logout/$',               authviews.logout, {'next_page' : "/"}),
    (r'^password_change/$',      authviews.password_change),
    (r'^password_reset/$',       authviews.password_reset),
    (r'^password_reset/done/$',  authviews.password_reset_done),
    (r'^register/$',             register),
)
