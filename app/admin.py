from django.contrib import admin
from .models import *

class AppAdmin(admin.ModelAdmin):
    list_display = ['english','french','arabic','field']
    list_editable = ['field']
    #search_fields = ['field']
    list_filter = ['field']


admin.site.register(MathWord,AppAdmin)
admin.site.register(PCWord,AppAdmin)
admin.site.register(SVTWord,AppAdmin)
admin.site.site_header = "ExoMoro"
admin.site.site_title = "ExoMoro admin page" 
