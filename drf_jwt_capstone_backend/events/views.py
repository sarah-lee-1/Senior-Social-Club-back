from django.shortcuts import render 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from .serializers import EventSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.http.response import Http404 
from .models import Event 
User = get_user_model()


# Admin/Events 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_event(request):
    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(event=request.event)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
   

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_event(request, pk):
    try:
        return Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        raise Http404 


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_event(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DEL'])
@permission_classes([IsAuthenticated])
def delete_event(request, pk):
    try:
        event = Event.objects.get(id=pk)
        serializer = EventSerializer(event)
        event.delete()
        return Response(serializer.data)
    except Event.DoesNotExist:
        raise Http404 


# User/Events 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_all_events(request, event):
    event = Event.objects.all()
    serializer = EventSerializer(event, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def rsvp_event(request, pk):
    rsvp = Event.objects.get(id=pk)
    serializer = EventSerializer(rsvp, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.erros, status=statusHTTP_404_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_event_map(request):
    rsvp_map = Event.objects.all()
    serializer = EventSerializer
    serializer = EventSerializer(rsvp_map,many=True)
    return Event(serializer.data)