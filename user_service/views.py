from django.shortcuts import render

from rest_framework import viewsets, mixins
from rest_framework import status

from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from .models import Profile

class UserViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
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
