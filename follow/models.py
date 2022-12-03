from django.db import models

# Create your models here.

BUILDING        = (
    ('','اختار المبني'),
    ('رياض أطفال','رياض أطفال'),
    ('معاذ ابن جبل','معاذ ابن جبل'),
    ('أبو بكر الصديق','أبو بكر الصديق'),
    ('إعدادي وثانوي','إعدادي وثانوي'),
    ('الامريكية','الامريكية'),
    ('الامريكية الجديد','الامريكية الجديد'),
    ('الإدارة','الإدارة'),
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
    build           = models.ForeignKey('Building',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Building(models.Model):
    b_name          = models.CharField(choices=BUILDING,max_length=30, null=True, blank=True)
    stage           = models.CharField(max_length=30, null=True, blank=True)
    it_support      = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self) -> str:
        return self.b_name

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

    