from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below

# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate

class SocialClub(models.Model):
    name =  models.CharField(max_length=200) 
    