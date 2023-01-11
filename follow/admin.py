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
    # search_fields   = ['firstname','lastname','email','situation']
    # list_filter     = ['situation','firstname']
    list_per_page       = 10

class BuildingAdmin(admin.ModelAdmin):
    form = BuildingForm
    list_display = ['b_name','stage' ,'user']
    search_fields   = ['stage','b_name']
    list_filter     = ['b_name','stage','user']
    list_per_page = 10

class Add_DVRAdmin(admin.ModelAdmin):
    form = Add_DVRForm
    list_display = ['name','floor' ,'ips','ports','build']
    search_fields   = ['name','floor','ips','ports']
    list_filter     = ['name','ips',]
    list_per_page = 10

class DVR_infoAdmin(admin.ModelAdmin):
    form = DVR_infoForm
    list_display = ['dvr','dvr_typ' ,'dvr_ip','dvr_cam_connect','dvr_cam_place']
    search_fields   = ['dvr','dvr_cam_place','dvr_ip','dvr_ports']
    list_filter     = ['dvr','dvr_ip',]
    list_per_page = 10

admin.site.register(DVR_info, DVR_infoAdmin)
admin.site.register(Add_DVR, Add_DVRAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Follow, FollowAdmin)
