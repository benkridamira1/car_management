from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):

    def displayImage(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))
    displayImage.short_description='Photo'
    list_display=('id', 'displayImage','first_name', 'designation' , 'created_date')
    list_display_links = ('id', 'first_name' ,'designation' )
    search_fields=('first_name','last_name' , 'designation')

admin.site.register(Team,TeamAdmin)