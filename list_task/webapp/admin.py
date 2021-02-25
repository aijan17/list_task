from django.contrib import admin
from webapp.models import Task

admin.site.register(Task)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'pub_date']
    list_filter = ['description']
    search_fields = ['description', 'status']
    fields = ['description', 'status', 'pub_date']
    readonly_fields = ['pub_date']