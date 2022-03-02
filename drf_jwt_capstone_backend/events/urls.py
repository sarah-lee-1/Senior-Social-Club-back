# Part 1                    Part 2                              Part 3
# 127.0.0.1:8000/           events/                             add_event/
# localsettings.py          drf_jwt_capstone_backen urls.py     events urls.py 


from django.contrib import admin 
from django.urls import path 
from events import views 


urlpatterns = [
   # Admin
    path('create_event/', views.create_event),
    path('view_event/<int:pk>/', views.view_event),
    path('view_all_events/', views.view_all_events), 
    path('update_event/<int:pk>/', views.update_event), 
    path('delete_event/<int:pk>/', views.delete_event),
 
    # # Member 
    # path('rsvp_event/<int:pk>/', views.rsvp_event), 
    # path('view_event_map/', views.view_event_map),
]

