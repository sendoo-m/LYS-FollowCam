# Generated by Django 3.2 on 2022-12-10 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0006_follow_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_dvr',
            name='build',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='follow.building'),
        ),
        migrations.AlterField(
            model_name='building',
            name='b_name',
            field=models.CharField(blank=True, choices=[('', 'اختار المبني'), ('رياض أطفال', 'رياض أطفال'), ('روضة الاطفال', 'روضة الاطفال'), ('معاذ ابن جبل', 'معاذ ابن جبل'), ('أبو بكر الصديق', 'أبو بكر الصديق'), ('إعدادي وثانوي', 'إعدادي وثانوي'), ('الامريكية', 'الامريكية'), ('الامريكية الجديد', 'الامريكية الجديد'), ('الإدارة', 'الإدارة')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='it_support',
            field=models.CharField(blank=True, choices=[('', 'المهندس المسؤل'), ('م. محمد جمال', 'م. محمد جمال'), ('م. محمود خير', 'م. محمود خير'), ('م. محمد شوقي', 'م. محمد شوقي'), ('م. أحمد يونس', 'م. أحمد يونس'), ('م. شحاته عبدالعزيز', 'م. شحاته عبدالعزيز')], max_length=30, null=True),
        ),
    ]
