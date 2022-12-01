from django.shortcuts import render
from .models import *

# Create your views here.

def add_dvr(request):
    
    return render(request, 'form/dvr_form.html' , {})

def all_dvr(request):
    
    context = {
        'all_dvr1' :Add_DVR.objects.all(),
        'all_dvr2' :Building.objects.all()
        }
    return render(request, 'form/all_dvr.html' , context)