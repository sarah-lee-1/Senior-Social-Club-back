from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from .serializers import MemberSerializer
from django.http.response import Http404
from .models import Member
User = get_user_model()



@api_view(['POST'])
# # @permission_classes([AllowAny])
def create_member(request):
    if request.method == "POST":
        serializer = MemberSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET'])
# @permission_classes([AllowAny])
def view_all_members(request):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)


# User/Members 
@api_view(['POST'])
# @permission_classes([AllowAny])
def create_membership_request(request):
    # memberRequest = request.user
    if request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # memberRequest.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def view_profile(request, pk):
    try:
        member = Member.objects.get(id=pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)
    except Member.DoesNotExist:
        raise Http404


@api_view(['PUT'])
@permission_classes([AllowAny]) 
def update_profile(request, pk):
    # print(f"update_profile ({request}, {pk})")
    profile = Member.objects.get(id=pk)
    serializer = MemberSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([AllowAny]) 
def update_member(request, pk):
    # print(f"update_profile ({request}, {pk})")
    profile = Member.objects.get(id=pk)
    serializer = MemberSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# @permission_classes([AllowAny])
# def view_profile(request, pk):
#     try:
#         profile = Member.objects.get(id=pk)
#         serializer = MemberSerializer(profile)
#         return Response(serializer.data)
#     except Member.DoesNotExist:
#         raise Http404

# def update_profile[(request, pk):
#     profile = Member.objects.get(id=pk)
#     serializer = MemberSerializer(member, data=request.data)
#     if serializer.is_valid():
#         profile.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


# TRY THIS
# @api_view(['POST', 'GET'])
# # # @permission_classes([AllowAny])
# def create_member(request):
#     newMember = request.user
#     if request.method == "POST":
#         serializer = MemberSerializer(data = request.data)
#         if serializer.is_valid():
#             newMember.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
#         elif request.method == 'GET':
#             member = Member.objects.filter(user_id=request.user.id)
#             serializer = MemberSerializer(member, many=True)
#             return Response(serializer.data) 

