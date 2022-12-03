from django.contrib import admin
from .models import *
from .forms import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
# Admin Panel 
admin.site.site_header  = 'LYS Follow CAM v 22.1.0 system Admin'
admin.site.index_title  = "Table of Follow DVR"

class FollowAdmin(ImportExportModelAdmin):  # ImportExportModelAdmin بديله عن   admin.ModelAdmin 
    # radio_fields    = {"smoker": admin.HORIZONTAL} # to convert in admin panel to horizontal
    form                = FollowForm
    # exclude         = ['status'] # لإظهار الحالة والتحكم فيها
    # list_display        = ['']
    # search_fields   = ['firstname','lastname','email','situation']
    # list_filter     = ['situation','firstname']
    list_per_page       = 10

admin.site.register(Add_DVR)
admin.site.register(Building)
admin.site.register(Follow,FollowAdmin)
