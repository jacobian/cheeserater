import urllib
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from cheeserater.packages.models import Package, Topic, Category
from cheeserater.votes.models import Vote
from django.views.generic import list_detail
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

def package_detail(request, name=None, package=None, template_name="packages/detail.html"):
    if package is None:
        package = get_object_or_404(Package, name=urllib.unquote_plus(name))
    return render_to_response(template_name, {
            "package" : package,
            "ctype"   : ContentType.objects.get_for_model(package),
            "score"   : Vote.objects.get_score(package),
        }, 
        RequestContext(request, {})
    )
    
def homepage(request):
    package = Package.objects.order_by("?")[0]
    return package_detail(request, package=package, template_name="homepage.html")

def topic_detail(request, topic_slug):
    topic = get_object_or_404(Topic, slug=topic_slug)
    return list_detail.object_list(
        request              = request,
        queryset             = topic.categories.all(),
        template_name        = "packages/topic.html",
        template_object_name = "category",
        paginate_by          = 100,
        extra_context        = {"topic" : topic},
    )

def category_detail(request, topic_slug, category_slug):
    category = get_object_or_404(Category, topic__slug=topic_slug, slug=category_slug)
    return list_detail.object_list(
        request              = request,
        queryset             = category.packages.all(),
        template_name        = "packages/list.html",
        template_object_name = "package",
        paginate_by          = 100,
        extra_context        = {"category" : category},
    )
    
def search(request):
    q = request.GET.get("q", "")
    if q and len(q) >= 3:
        clause = Q(name__icontains=q)                   \
               | Q(keywords__icontains=q)               \
               | Q(summary__icontains=q)                \
               | Q(categories__value__icontains=q)      \
               | Q(categories__topic__name__icontains=q)
        qs = Package.objects.filter(clause).distinct()
    else:
        qs = Package.objects.none()
        
    return list_detail.object_list(
        request              = request,
        queryset             = qs,
        template_name        = "packages/search.html",
        template_object_name = "package",
        paginate_by          = 100,
        extra_context        = {"q" : q},
    )

def packages_by_score(request):
    top, bottom = [], []
    for query, list_ in [(Vote.objects.get_top, top), (Vote.objects.get_bottom, bottom)]:
        for package, score in query(Package, 10):
            package.score = score
            list_.append(package)
    
    return render_to_response("packages/top.html", {
            "top" : top,
            "bottom" : bottom,
        }, RequestContext(request, {})
    )
