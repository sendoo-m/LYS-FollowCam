# Generated by Django 3.2 on 2023-01-11 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0012_alter_add_dvr_build'),
    ]

    operations = [
        migrations.CreateModel(
            name='DVR_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dvr_typ', models.CharField(blank=True, max_length=30, null=True)),
                ('drv_mic', models.CharField(blank=True, max_length=30, null=True)),
                ('dvr_ports', models.CharField(blank=True, max_length=30, null=True)),
                ('dvr_cam_connect', models.CharField(blank=True, max_length=30, null=True)),
                ('dvr_cam_ports', models.CharField(blank=True, max_length=30, null=True)),
                ('dvr_ip', models.CharField(blank=True, max_length=30, null=True)),
                ('dvr_notes', models.TextField(blank=True, max_length=30, null=True)),
                ('dvr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow.add_dvr')),
            ],
        ),
    ]
