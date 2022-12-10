from django.shortcuts import render
from .models import *
from .forms import *

##====================================##
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required # login required to access private pages.
from django.views.decorators.cache import cache_control # Destory the section after log out.
# from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q # for search
# Concatenated F-name and L-name
from django.db.models.functions import Concat # Concatenated
from django.db.models import Value as P #(P=Plus)

##====================================##
# Create your views here.
@login_required(login_url='user-login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_dvr(request):
    if request.method == "POST":

        form = Add_DVRForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "DVR Added successfully !")
            return HttpResponseRedirect('/')
        else:
            context = {
                "form":form
            }
            return render(request, 'follow/dvr_form.html', context)
    else:
        form    = Add_DVRForm()
        context = {
                "form":form
            }
    return render(request, 'follow/dvr_form.html' , context)


@login_required(login_url='user-login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def all_dvr(request):
    
    context = {
        'all_dvr1' :Add_DVR.objects.all().order_by('ips'),
        'all_dvr2' :Building.objects.all(),
        }
    return render(request, 'follow/all_dvr.html' , context)


@login_required(login_url='user-login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_build(request):
    if request.method == "POST":

        form = BuildingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "build Added successfully !")
            return HttpResponseRedirect('/')
        else:
            context = {
                "form":form
            }
            return render(request, 'follow/add_build.html', context)
    else:
        form    = BuildingForm()
        context = {
                "form":form
            }
    return render(request, 'follow/add_build.html' , context)

@login_required(login_url='user-login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def follow_dvr(request):
    if request.method == "POST":

        form = FollowForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "تم اضافة التقرير بنجاح")
            return HttpResponseRedirect('/')
        else:
            context = {
                "form":form
            }
            return render(request, 'follow/follow_dvr.html', context)
    else:
        form    = FollowForm()
        context = {
                "form":form
            }

    return render(request, 'follow/follow_dvr.html', context)



@login_required(login_url='user-login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def follow_results(request):
    context = {
        'follow_results' :Follow.objects.all()
        }
    return render(request, 'follow/follow_results.html' , context)
