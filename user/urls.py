from django.contrib import admin
from django.urls import path
from . import views 
from user import views as user_view
from django.contrib.auth import views as auth_views


app_name = 'user'
urlpatterns = [
    # path('', views.register, name='user-register'),
    path('login/', views.login, name='user-login'),
    path('logout/', views.logout, name='user-logout'),
    path('profile_update/', user_view.profile_update, name='user-profile-update'),
    # path('profile_update/', views.profile_update, name='user-profile-update')
    # path('user/', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),
    
] 