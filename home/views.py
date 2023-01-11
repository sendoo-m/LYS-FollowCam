from django.shortcuts import render
from django.contrib.auth.decorators import login_required # login required to access private pages.
from django.views.decorators.cache import cache_control # Destory the section after log out.
from follow.views import *
from follow.models import *
from follow.forms import *
from django.core.paginator import Paginator, PageNotAnInteger
# from .filters import FollowFilter
from datetime import date
from datetime import datetime, timedelta
# Create your views here.


@login_required(login_url='user-login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    all_dvr1         = Add_DVR.objects.all().order_by('name')
    all_dvr2         = Building.objects.all().order_by('-b_name')
    follow_results = Follow.objects.filter(created_at__date=date.today())

    # Add pagination to follow_results
    paginator = Paginator(follow_results, 10)  # Show 10 results per page
    page = request.GET.get('page')
    try:
        follow_results = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        follow_results = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        follow_results = paginator.page(paginator.num_pages)

    context = {
        'all_dvr1' : all_dvr1,
        'all_dvr2' : all_dvr2,
        'follow_results': follow_results,
    }
    return render(request, 'home/home.html', context)