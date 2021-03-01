from django.contrib import admin
from webapp.models import Task

admin.site.register(Task)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description','text_for_detailed', 'status', 'pub_date']
    list_filter = ['description']
    search_fields = ['description', 'status']
    fields = ['description', 'status', 'pub_date']
    readonly_fields = ['pub_date']