from django.contrib import admin
from django.urls import path 
from members import views 


urlpatterns = [
    # Admin
    path('create_member/', views.create_member), 
    path('view_all_members/', views.view_all_members),
    # path('update_member/', views.update_member),
    
    
    # Member
    # path('request_membership/', views.create_membership_request), 
    # path('create_profile/', views.create_profile), 
    # path('view_profile/', views.view_profile), 
    # path('update_profile/',  views.update_profile),
    # path('view_balance/', views.view_balance), 
]
