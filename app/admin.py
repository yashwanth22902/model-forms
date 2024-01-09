from django.contrib import admin
from app.models import *

# Register your models here.

class customizeAcessRecord(admin.ModelAdmin):
    list_display=['name','date','author','email']
    list_display_links=['name']
    list_editable=['author']
    list_filter=['email']
    search_fields=['author']
    list_select_related=['name']
    list_per_page=1

class customizeWebpage(admin.ModelAdmin):
    list_display=['topic_name','url','name']
    list_display_links=['name']


admin.site.register(Topic)

admin.site.register(Webpage,customizeWebpage)

admin.site.register(AcessRecord,customizeAcessRecord)
