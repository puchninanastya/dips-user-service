from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from .models import Profile

#TODO: Create tests for views
#TODO: Create pagination
#TODO: Return to super views?

class UserViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
