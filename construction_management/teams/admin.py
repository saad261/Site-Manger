from django.contrib import admin

from .models import Team
from .models import Task
from .models import Location
from .models import Site


#admin.site.register(Location)
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fields = ("code", ('area', 'location', 'additional'), "site")
    list_display = ('code', 'site')
    list_filter = ('code', 'site')
    ordering = ('code',)
    search_fields = ('code', 'site')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    fields = ("name", ('phone_number', 'email'), "task")
    list_display = ('name', 'phone_number')
    list_filter = ('name', 'task')
    ordering = ('name',)
    search_fields = ('name', 'phone_number', "task")

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = (('task_name', 'starting_date'), "location")
    list_display = ('task_name', 'starting_date')
    list_filter = ('location', 'starting_date')
    ordering = ('starting_date',)
    search_fields = ('task_name', 'starting_date', "location")

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    fields = ("site_name", ('address', 'link'), "manager", 'site_image')
    list_display = ('site_name',)
    list_filter = ('manager', "site_name")
    ordering = ('manager',)
    search_fields = ('site_name', 'manager')

