from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from .serializers import MemberSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.http.response import Http404
from .models import Member 
User = get_user_model()

# Create your views here.
# Admin/Members
# approve_member
# update_member
# view_members 



# User/Members 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_membership_request(request):
    if request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 
@api_view(['POST', 'GET'])
def create_profile(request, pk):
    if request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        profile = Member.objects.post(user_id=request.user.id)
        serializer = MemberSerializer(profile)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_profile(request, pk):
    try:
        profile = Member.objects.get(id=pk)
        serializer = MemberSerializer(profile)
        return Response(serializer.data)
    except Member.DoesNotExist:
        raise Http404 


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request, pk):
    profile = Member.objects.get(id=pk)
    serializer = MemberSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_balance(request, balance):
    try:
        balance = Member.objects.get(id=pk)
        serializer = MemberSerializer(balance)
        return Response(serializer.data)
    except Balance.DoesNotExist:
        raise Http404 
