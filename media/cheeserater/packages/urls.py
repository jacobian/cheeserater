from django.conf.urls.defaults import *
from django.views.generic import list_detail
from cheeserater.packages.models import Package, Topic
from cheeserater.packages.views import topic_detail, package_detail, category_detail, search, packages_by_score

package_info = {
    "queryset"              : Package.objects.all(),
    'template_object_name'  : "package",
    'template_name'         : "packages/list.html",
    'paginate_by'           : 100,
}

topic_info = {
    "queryset"              : Topic.objects.all(),
    'template_object_name'  : "topic",
    'template_name'         : "packages/topic_list.html",
}

urlpatterns = patterns('',
    (r'^$',                                                                 list_detail.object_list, package_info),
    (r'^by-category/$',                                                     list_detail.object_list, topic_info),
    (r'^by-category/(?P<topic_slug>[\w-]+)/$',                              topic_detail),
    (r'^by-category/(?P<topic_slug>[\w-]+)/(?P<category_slug>[\w-]+)/$',    category_detail),
    (r'^by-score/$',                                                        packages_by_score),
    (r'^search/$',                                                          search),
    (r'^(?P<name>.*)/$',                                                    package_detail),
)


