# Generated by Django 3.2 on 2022-12-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0004_alter_follow_hdd_alter_follow_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='hdd',
            field=models.CharField(blank=True, choices=[('', 'اختار الحالة'), ('يعمل بكفائه', 'يعمل بكفائه'), ('توجد مشكلة', 'توجد مشكلة'), ('تم حل المشكلة', 'تم حل المشكلة'), ('تم تغيير القطعة', 'تم تغيير القطعة')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='follow',
            name='images',
            field=models.CharField(blank=True, choices=[('', 'اختار الحالة'), ('يعمل بكفائه', 'يعمل بكفائه'), ('توجد مشكلة', 'توجد مشكلة'), ('تم حل المشكلة', 'تم حل المشكلة'), ('تم تغيير القطعة', 'تم تغيير القطعة')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='follow',
            name='lan',
            field=models.CharField(blank=True, choices=[('', 'اختار الحالة'), ('يعمل بكفائه', 'يعمل بكفائه'), ('توجد مشكلة', 'توجد مشكلة'), ('تم حل المشكلة', 'تم حل المشكلة'), ('تم تغيير القطعة', 'تم تغيير القطعة')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='follow',
            name='mic',
            field=models.CharField(blank=True, choices=[('', 'اختار الحالة'), ('يعمل بكفائه', 'يعمل بكفائه'), ('توجد مشكلة', 'توجد مشكلة'), ('تم حل المشكلة', 'تم حل المشكلة'), ('تم تغيير القطعة', 'تم تغيير القطعة')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='follow',
            name='power',
            field=models.CharField(blank=True, choices=[('', 'اختار الحالة'), ('يعمل بكفائه', 'يعمل بكفائه'), ('توجد مشكلة', 'توجد مشكلة'), ('تم حل المشكلة', 'تم حل المشكلة'), ('تم تغيير القطعة', 'تم تغيير القطعة')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='follow',
            name='record',
            field=models.CharField(blank=True, choices=[('', 'اختار الحالة'), ('يعمل بكفائه', 'يعمل بكفائه'), ('توجد مشكلة', 'توجد مشكلة'), ('تم حل المشكلة', 'تم حل المشكلة'), ('تم تغيير القطعة', 'تم تغيير القطعة')], max_length=30, null=True),
        ),
    ]
