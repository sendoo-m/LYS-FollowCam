from django.contrib import admin
from django.urls import path
from . import views 


app_name = 'user'
urlpatterns = [
    # path('', views.register, name='user-register'),
    path('login/', views.login, name='user-login'),
    path('logout/', views.logout, name='user-logout'),
    
] 