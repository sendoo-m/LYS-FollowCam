from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    email       = forms.EmailField()


    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        managed = True
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        fields = ['address','phone', 'image']