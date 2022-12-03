from django.shortcuts import render
from .models import *

# Create your views here.

def add_dvr(request):
    
    return render(request, 'follow/dvr_form.html' , {})

def all_dvr(request):
    
    context = {
        'all_dvr1' :Add_DVR.objects.all(),
        'all_dvr2' :Building.objects.all()
        }
    return render(request, 'follow/all_dvr.html' , context)

def follow_dvr(request):
    context = {
        
        }
    return render(request, 'follow/follow_dvr.html', context)