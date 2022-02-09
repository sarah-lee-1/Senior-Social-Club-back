"""drf_jwt_capstone_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from events import views 
# from members import views 
# from social_clubs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    
    # Admin
    path('approve_member/', views.create_member), 
    path('update_member/', views.update_member),
    path('view_members/', views.view_all_members), 
    
    path('create_event/', views.create_event), 
    path('view_event/', views.view_event), 
    path('update_event/', views.update_event), 
    path('delete_event/', views.delete_event),
    
    # Member
    path('request_membership/', views.create_membership_request), 
    path('create_profile/', views.create_profile), 
    path('view_profile/', views.view_profile), 
    path('update_profile/',  views.update_profile),
    path('view_balance/', views.view_balance), 
    
    path('events/', views.view_all_events), 
    path('rsvp_event/', views.rsvp_event), 
    path('rsvp_map/', views.view_event_map),
    
]
