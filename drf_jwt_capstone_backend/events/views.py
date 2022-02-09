from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from .serializers import EventSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
User = get_user_model()


# Create your views here.
# Admin/Events 
# create_event
# update_event
# delete_event 
# view_events 


# User/Events
# view_events
# rsvp_events
# view_rsvp_map
