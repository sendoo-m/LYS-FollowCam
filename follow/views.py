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
from django.core.paginator import Paginator, PageNotAnInteger
from .filters import FollowFilter
from datetime import date
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404

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

# for registrations DVR and Info and create it by forms
@login_required(login_url='user-login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_dvr_info(request):
    if request.method == "POST":

        form = DVR_infoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "DVR Added successfully !")
            return HttpResponseRedirect('/')
        else:
            context = {
                "form":form
            }
            return render(request, 'follow/add_dvr_info.html', context)
    else:
        form    = DVR_infoForm()
        context = {
                "form":form
            }
    return render(request, 'follow/add_dvr_info.html' , context)

#to create list of DVR
@login_required(login_url='user-login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dvr_info(request):
    context = {
        'dvr_info' :DVR_info.objects.all().order_by('dvr_ip'),
        }
    return render(request, 'follow/dvr_info.html' , context)

# to create individual info of DVR
@login_required(login_url='user-login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def about_dvr(request, id):
    about_dvr = get_object_or_404(DVR_info, id=id)
    context = {
        'about_dvr' : about_dvr,
        }
    return render(request, 'follow/about_dvr.html' , context)


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
    # follow_results = Follow.objects.filter(created_at__date=date.today())
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    follow_results = Follow.objects.filter(created_at__range=[start_date, end_date])
    if request.method == 'GET':
        form = FollowFilterForm(request.GET)
        if form.is_valid():
            user = form.cleaned_data['user']
            
            # dvr_name = form.cleaned_data['dvr_name']
            if user:
                follow_results = follow_results.filter(user=user)
            # if dvr_name:
            #     follow_results = follow_results.filter(dvr_name__icontains=dvr_name)
    else:
        form = FollowFilterForm()
    # Add pagination to the view
    paginator = Paginator(follow_results, 10)
    page = request.GET.get('page')
    try:
        follow_results = paginator.page(page)
    except PageNotAnInteger:
        follow_results = paginator.page(1)
    except EmptyPage:
        follow_results = paginator.page(paginator.num_pages)

    context = {
        'form': form,
        'follow_results': follow_results
    }
    return render(request, 'follow/follow_results.html', context)

from datetime import datetime, timedelta

# def follow_all_results(request):
#     end_date = datetime.now()
#     start_date = end_date - timedelta(days=30)
#     follow_results = Follow.objects.filter(created_at__range=[start_date, end_date])
#     paginator = Paginator(follow_results, 10)
#     page = request.GET.get('page')
#     try:
#         follow_results = paginator.page(page)
#     except PageNotAnInteger:
#         follow_results = paginator.page(1)
#     except EmptyPage:
#         follow_results = paginator.page(paginator.num_pages)

#     context = {
#         'follow_all_results': follow_results
#     }
#     return render(request, 'follow/follow_all_results.html', context)


