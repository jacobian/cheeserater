import xmlrpclib
from django.template.defaultfilters import slugify
from cheeserater.packages.models import Package, Topic, Category

CHEESESHOP = "http://cheeseshop.python.org/pypi"

def main():
    s = xmlrpclib.Server(CHEESESHOP)
    for name in sorted(s.list_packages(), key=lambda s: s.lower()):
        print "Updating %r" % name
        # Load info from the cheeseshop
        versions = s.package_releases(name)
    
        # Use the latest version
        try:
            info = s.release_data(name, versions[-1])
        except IndexError:
            print "Skipping %r: no versions" % name
            continue
    
        # Lookup or create the package object
        try:
            package = Package.objects.get(name=name)
        except Package.DoesNotExist:
            package = Package(name=name)
            print "Created package %r" % name
    
        # Update package fields
        package.version = versions[-1]
        for f in ['author', 'description', 'home_page', 'keywords', 'summary']:
            value = info.get(f, "")
            if value is None or value.strip() == "UNKNOWN":
                value = ""
            value = value.strip()
            setattr(package, f, value)
        package.save()

        # Handle categories
        categories = []
        for classifier in info["classifiers"]:
            topic, value = map(str.strip, classifier.split("::", 1))
            topic, created = Topic.objects.get_or_create(
                name     = topic, 
                defaults = {"slug": slugify(topic)[:50]}
            )
            if created: print "Created topic %r" % topic.name
            
            cat, created = Category.objects.get_or_create(
                topic    = topic, 
                value    = value, 
                defaults = {"slug": slugify(value)[:50]}
            )
            if created: print "Created category '%s'" % cat
                
            categories.append(cat)
            
        package.categories = categories
        
if __name__ == '__main__':
    main()