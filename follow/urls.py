from django.urls import path
from .import views 

urlpatterns = [

    path('', views.add_dvr , name='add_dvr'),
    path('add_build/', views.add_build , name='add_build'),
    path('all_dvr/', views.all_dvr , name='all_dvr'),
    path('follow_dvr/', views.follow_dvr , name='follow_dvr'),
    path('follow_results/', views.follow_results , name='follow_results'),
    path('dvr_info/', views.dvr_info , name='dvr_info'),
    path('about_dvr/<int:id>/', views.about_dvr , name='about_dvr'),
    
]