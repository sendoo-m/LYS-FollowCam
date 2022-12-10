from django.shortcuts import render
from django.contrib.auth.decorators import login_required # login required to access private pages.
from django.views.decorators.cache import cache_control # Destory the section after log out.
from follow.views import *
from follow.models import *
from follow.forms import *
# Create your views here.


@login_required(login_url='user-login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(requset):
    all_dvr1         = Add_DVR.objects.all().order_by('name')
    all_dvr2         = Building.objects.all().order_by('-b_name')
    follow_results   = Follow.objects.all().order_by('created_at')
    
    context = {
        'all_dvr1' : all_dvr1,
        'all_dvr2' : all_dvr2,
        'follow_results' : follow_results,
        }
    return render(requset, 'home/home.html', context)