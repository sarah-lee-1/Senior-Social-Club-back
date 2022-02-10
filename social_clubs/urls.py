from django.contrib import admin
from django.urls import path 
from . import views 


urlpatterns = [
    # Admin
    path('social_club/', views.social_club), 
]
