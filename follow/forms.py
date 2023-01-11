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
        
class FollowFilterForm(forms.Form):
    class Meta:
        model       = Follow
        # fields      = '__all__'

    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    
    # dvr_name = forms.CharField(max_length=100, required=False)

class DVR_infoForm(forms.ModelForm):
    class Meta:
        model       = DVR_info
        fields      = '__all__'