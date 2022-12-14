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
            messages.success(request, "???? ?????????? ?????????????? ??????????")
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



# @login_required(login_url='user-login')
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def follow_results(request):
#     # Get the page number from the request query string
#     # If no page number is specified, default to page 1
#     page_number = request.GET.get('page', 1)

#     # Create a Paginator object with a specified number of items per page
#     paginator = Paginator(Follow.objects.all(), 10)

#     # Use the Paginator object to get the specified page of results
#     follow_results = paginator.get_page(page_number)
#     follow_results_list = Follow.objects.all()
#     follow_results_filter = FollowFilter(request.GET, queryset=follow_results_list)
#     context = {
#         'follow_results' :Follow.objects.all(),
#         'follow_results_filter': follow_results_filter,
#         }
#     return render(request, 'follow/follow_results.html' , context)
@login_required(login_url='user-login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def follow_results(request):
    follow_results = Follow.objects.all()
    if request.method == 'GET':
        form = FollowFilterForm(request.GET)
        if form.is_valid():
            user = form.cleaned_data['user']
            
            dvr_name = form.cleaned_data['dvr_name']
            if user:
                follow_results = follow_results.filter(user=user)
            if dvr_name:
                follow_results = follow_results.filter(dvr_name__icontains=dvr_name)
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



# def create_building_permissions():
#     # Get or create the `Abo Bakr` group
#     building_1_group, created = Group.objects.get_or_create(name='Abo Bakr')
#     # Get the `Can view Abo Bakr` permission
#     building_1_view_permission = Permission.objects.get(name='Can view Abo Bakr')
#     # Add the `Can view Abo Bakr` permission to the `Abo Bakr` group
#     building_1_group.permissions.add(building_1_view_permission)
#     # Save the `Abo Bakr` group
#     building_1_group.save()

#     # Repeat the process for the `Administrator Build` group
#     building_2_group, created = Group.objects.get_or_create(name='Administrator Build')
#     building_2_view_permission = Permission.objects.get(name='Can view Administrator Build')
#     building_2_group.permissions.add(building_2_view_permission)
#     building_2_group.save()

#     # Repeat the process for the `KG` group
#     building_2_group, created = Group.objects.get_or_create(name='KG')
#     building_2_view_permission = Permission.objects.get(name='Can view KG')
#     building_2_group.permissions.add(building_2_view_permission)
#     building_2_group.save()

#     # Repeat the process for the `New American` group
#     building_2_group, created = Group.objects.get_or_create(name='New American')
#     building_2_view_permission = Permission.objects.get(name='Can view New American')
#     building_2_group.permissions.add(building_2_view_permission)
#     building_2_group.save()

#     # Repeat the process for the `American` group
#     building_2_group, created = Group.objects.get_or_create(name='American')
#     building_2_view_permission = Permission.objects.get(name='Can view American')
#     building_2_group.permissions.add(building_2_view_permission)
#     building_2_group.save()

#     # Repeat the process for the `Moaaz` group
#     building_2_group, created = Group.objects.get_or_create(name='Moaaz')
#     building_2_view_permission = Permission.objects.get(name='Can view Moaaz')
#     building_2_group.permissions.add(building_2_view_permission)
#     building_2_group.save()

#     # Repeat the process for the `Prep and Secondary` group
#     building_2_group, created = Group.objects.get_or_create(name='Prep and Secondary')
#     building_2_view_permission = Permission.objects.get(name='Can view Prep and Secondary')
#     building_2_group.permissions.add(building_2_view_permission)
#     building_2_group.save()

    
# # Run the `create_building_permissions` function
# create_building_permissions()
