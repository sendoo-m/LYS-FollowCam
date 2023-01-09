from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
# Create your models here.

class Profile(models.Model):
    staff          = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address        = models.CharField(max_length=200, null=True)
    phone          = models.CharField(max_length=20, null=True)
    image          = models.ImageField(default='avatar.jpg', upload_to='Profile_Images')

    def __str__(self):
        return f'{self.staff.username}-profile'


class MyUser(AbstractUser):
    building_permission = models.CharField(max_length=200, blank=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_permissions')