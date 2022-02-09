# Part 1                    Part 2                              Part 3
# 127.0.0.1:8000/           events/                             add_event/
# localsettings.py          drf_jwt_capstone_backen urls.py     events urls.py 

from django.contrib import admin 
from django.urls import path 
from events import views 


urlpatterns = [
    # Admin
    path('create_event/', views.create_event), 
    path('view_event/', views.view_event), 
    path('update_event/', views.update_event), 
    path('delete_event/', views.delete_event),
    
    # Member
    path('events/', views.view_all_events), 
    path('rsvp_event/', views.rsvp_event), 
    path('rsvp_map/', views.view_event_map),
]
