from django.contrib import admin
from django.urls import path 
from members import views 


urlpatterns = [
    # Admin
    path('create_member/', views.create_member), 
    path('view_all_members/', views.view_all_members),
    
    # Member
    path('create_membership_request/', views.create_membership_request), 
    path('view_profile/<int:pk>/', views.view_profile), 
    path('update_profile/<int:pk>/', views.update_profile), 
    path('update_member/<int:pk>/', views.update_member), 
    # Admin can also update profile
]
