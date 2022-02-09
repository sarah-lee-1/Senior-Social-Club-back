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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('events/', include('events.urls')),
    path('members/', include('members.urls')),
    path('social_clubs/', include('social_clubs.urls')), 
    
    
   
    
    path('create_event/', views.create_event), 
    path('view_event/', views.view_event), 
    path('update_event/', views.update_event), 
    path('delete_event/', views.delete_event),
    

    
    path('events/', views.view_all_events), 
    path('rsvp_event/', views.rsvp_event), 
    path('rsvp_map/', views.view_event_map),
    
]
