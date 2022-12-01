from django.urls import path
from .import views 

urlpatterns = [

    path('', views.add_dvr , name='add_dvr'),
    path('all_dvr/', views.all_dvr , name='all_dvr'),

]