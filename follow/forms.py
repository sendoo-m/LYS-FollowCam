from django import forms
import datetime
from datetime import date
from .models import *
# from django.core.validators import RegexValidator # لعمل صلاحيات خاصة على الحقول 
# from django.core.exceptions import ValidationError # مستخدم في داله عدم تكرار المدخلات


class Add_DVRForm(forms.ModelForm):
    class Meta:
        model       = Add_DVR
        fields      = '__all__'

class BuildingForm(forms.ModelForm):
    class Meta:
        model       = Building
        fields      = '__all__'

class FollowForm(forms.ModelForm):
    class Meta:
        model       = Follow
        fields      = '__all__'
        