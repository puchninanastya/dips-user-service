from rest_framework import serializers
from .models import Profile

"""Serializers to map the model instances into JSON format."""

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('phone_number')

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name' 'profile')
