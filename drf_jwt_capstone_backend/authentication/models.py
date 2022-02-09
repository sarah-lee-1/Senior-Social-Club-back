from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below

# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


class User(AbstractUser):
    middle_name = models.CharField(max_length=20)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=15)
    zip_code = models.IntegerField()
    is_active = models.CharField(max_length=3)
    balance = models.IntegerField() 
    
class Event(models.Model):
    title = models.CharField(max_length= 200) 
    description = models.CharField(max_length=500) 
    month = models.CharField(max_length=9) 
    day = models.CharField(max_length=9) 
    year = models.CharField(max_length=4) 
    time = models.CharField(max_length=8)
    street = models.CharField(max_length=46)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)  
    
class Member(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length = 35)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=15)
    zip_code = models.IntegerField(max_length=5)
    is_active = models.CharField(max_length=3)
    balance = models.IntegerField()  

class SocialClub(models.Model):
    name =  models.CharField(max_length=200) 
