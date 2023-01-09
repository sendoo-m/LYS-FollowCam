from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User

# Create your models here.

BUILDING        = (
    ('','اختار المبني'),
    ('رياض أطفال','رياض أطفال'),
    ('روضة الاطفال','روضة الاطفال'),
    ('معاذ ابن جبل','معاذ ابن جبل'),
    ('أبو بكر الصديق','أبو بكر الصديق'),
    ('إعدادي وثانوي','إعدادي وثانوي'),
    ('الامريكية','الامريكية'),
    ('الامريكية الجديد','الامريكية الجديد'),
    ('الإدارة','الإدارة'),
)

ITSUPPORT       = (
    ('','المهندس المسؤل'),
    ('م. تامر خير','م. تامر خير'),
    ('م. محمد جمال','م. محمد جمال'),
    ('م. محمود خير','م. محمود خير'),
    ('م. محمد شوقي','م. محمد شوقي'),
    ('م. أحمد يونس','م. أحمد يونس'),
    ('م. شحاته عبدالعزيز','م. شحاته عبدالعزيز'),
)

FOLLOW          =(
    ('','اختار الحالة'),
    ('يعمل بكفائه','يعمل بكفائه'),
    ('توجد مشكلة','توجد مشكلة'),
    ('تم حل المشكلة','تم حل المشكلة'), 
    ('تم تغيير القطعة','تم تغيير القطعة'), 
)

class Add_DVR(models.Model):
    name            = models.CharField(max_length=30, null=True, blank=True)
    floor           = models.CharField(max_length=30, null=True, blank=True)
    ips             = models.CharField(max_length=30, null=True, blank=True)
    ports           = models.CharField(max_length=30, null=True, blank=True)
    build           = models.OneToOneField('Building',on_delete=models.CASCADE)

    def __str__(self):
        if not self.name:
            return ""
        return str(self.name)
    
class Building(models.Model):
    b_name          = models.CharField(choices=BUILDING,max_length=30, null=True, blank=True)
    stage           = models.CharField(max_length=30, null=True, blank=True)
    it_support      = models.CharField(choices=ITSUPPORT,max_length=30, null=True, blank=True)
    user            = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return self.b_name or ''

class Follow(models.Model):
    dvr             = models.ForeignKey(Add_DVR, on_delete=models.CASCADE )
    images          = models.CharField(choices=FOLLOW, max_length=30, null=True, blank=True)
    mic             = models.CharField(choices=FOLLOW, max_length=30, null=True, blank=True)
    record          = models.CharField(choices=FOLLOW, max_length=30, null=True, blank=True)
    hdd             = models.CharField(choices=FOLLOW, max_length=30, null=True, blank=True)
    power           = models.CharField(choices=FOLLOW, max_length=30, null=True, blank=True)
    lan             = models.CharField(choices=FOLLOW, max_length=30, null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True, null=True, blank=True )
    notes           = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        if not self.dvr:
            return ""
        return str(self.dvr)
    