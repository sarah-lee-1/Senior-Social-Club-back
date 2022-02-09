from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below

# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate

class Member(models.Model):
    middle_name = models.CharField(max_length=20)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=15)
    zip_code = models.IntegerField()
    is_active = models.CharField(max_length=3)
    balance = models.IntegerField() 
    