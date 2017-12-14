from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    #username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Profile
        depth = 0
        fields = ('id', 'phone_number', 'birth_date')

class UserSerializer(serializers.ModelSerializer):
    #profile_id = serializers.ReadOnlyField(source='profile.id')
    id = serializers.IntegerField(source='pk', read_only=True)
    profile = ProfileSerializer()
    #phone_number = serializers.CharField(source='profile.phone_number')
    #birth_date = serializers.DateField(source='profile.birth_date')
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password',
            'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        if user is not None:
            password = validated_data.get('password', None)
            if password is not None:
                user.set_password(password)
                user.save()
        Profile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        #retrieve the Profile
        profile_data = validated_data.pop('profile', None)
        for attr, value in profile_data.items():
            setattr(instance.profile, attr, value)

        #retrieve the User
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        new_password = validated_data.get('password', None)
        if new_password is not None:
            instance.set_password(new_password)

        instance.profile.save()
        instance.save()
        return instance
