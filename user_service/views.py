from django.shortcuts import render
from django.contrib.auth import authenticate
from django.utils import timezone

from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from .models import Profile, UserToken, AppToken
from .token_auth import AppTokenAuthentication

import binascii
import os

class UserTokenView(APIView):
    authentication_classes = (AppTokenAuthentication, )

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        if (username is None or password is None):
            return Response({'error': 'Need username and password data'}, status=400)
        auth_user = authenticate(username=username, password=password)
        if auth_user is None:
            print('auth not ok')
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            print('auth is ok')
            new_token = binascii.hexlify(os.urandom(15)).decode('ascii')
            print(new_token)
            tok, created = UserToken.objects.update_or_create(
                user=auth_user,
                defaults={
                    'user': auth_user,
                    'token': new_token,
                    'expires': timezone.now() + timezone.timedelta(minutes=1)},
            )
            print('tok is')
            print(tok)
            print('created is')
            print(created)
            return Response({'token': new_token})


class UserTokenCheckView(APIView):
    def post(self, request):
        username = request.data['username']
        token = request.data['token']
        user = authenticate(username=username, password=password)
        try:
            tok = Token.objects.get(client_id=clientId, client_secret=clientSecret)
        except Token.DoesNotExist:
            return Response(status=401)
        if tok.expires < timezone.now():
            return Response(status=401)
        else:
            tok.expires = timezone.now() + timezone.timedelta(minutes=1)
            tok.save()
            return Response(status=200)

class AppTokenView(APIView):
    def get(self, request):
        clientId = request.query_params.get('clientId')
        clientSecret = request.query_params.get('clientSecret')
        try:
            tok = AppToken.objects.get(client_id=clientId, client_secret=clientSecret)
        except AppToken.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)
        new_token = binascii.hexlify(os.urandom(15)).decode('ascii')
        tok.token = new_token
        tok.expires = timezone.now() + timezone.timedelta(minutes=1)
        tok.save()
        return Response({'token': new_token})

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
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
