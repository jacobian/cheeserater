from django.contrib import admin
from cheeserater.packages.models import Topic, Category, Package

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ["value"]}

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ['name']}
      
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'summary')
    search_fields = ('name', 'summary', 'keywords')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Package, PackageAdmin)
