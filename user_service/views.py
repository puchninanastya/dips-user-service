from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from .models import Profile

# users/
class UserList(APIView):
  def get(self, request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# users/<id>
class UserDetail(APIView):
  def get(self, request, id):
    user = get_object_or_404(User, pk=id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

  def put(self, request, id):
    user = get_object_or_404(User, pk=id)
    serializer = UserSerializer(user,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# profiles/
class ProfileList(APIView):
  def get(self, request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# profiles/<id>
class ProfileDetail(APIView):
  def get(self, request, id):
    profile = get_object_or_404(Profile, pk=id)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)

  def put(self, request, id):
    profile = get_object_or_404(Profile, pk=id)
    serializer = ProfileSerializer(profile,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, id):
    profile = get_object_or_404(Profile, pk=id)
    profile.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
