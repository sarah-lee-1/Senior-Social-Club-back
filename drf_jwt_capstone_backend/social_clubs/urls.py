rom django.contrib import admin
from django.urls import path 
from social_clubs import views 


urlpatterns = [
    # Admin
    path('social_club/', views.social_club), 
]
