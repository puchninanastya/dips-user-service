from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class ModelTestCase(TestCase):
    """This class defines the test suite for the Profile model."""

    def setUp(self):
        newUser1 = User.objects.create_user(username='john007',
            first_name='John',
            second_name='Lennon',
            email='jlennon@beatles.com',
            password='beatlesrulit')
        profile1 = Profile.objects.create(user=newUser1, phone_number='+79161002030')
        newUser2 = User.objects.create_user(username='vasss',
            first_name='Vasya',
            second_name='Pupkin',
            email='vasss@gmail.com',
            password='qwerty123')
        profile2 = Profile.objects.create(user=newUser2, phone_number='+79094005060')
        newUser3 = User.objects.create_user(username='vasss',
            first_name='Vasya',
            second_name='Pupkin',
            email='vasss@gmail.com',
            password='qwerty123')
        profile3 = Profile.objects.create(user=newUser3, phone_number='+79094005060')
        newUser4 = User.objects.create_user(username='vano',
            first_name='Ivan',
            second_name='Ivanov',
            email='vano@yandex.ru',
            password='etomoiparol')
        profile4 = Profile.objects.create(user=newUser4, phone_number='+79151005060')

    def test_model_can_create_profile(self):
        """Test the bucketlist model can create a Profile."""
        old_count = Profile.objects.count()
        self.profile1.save()
        new_count = Profile.objects.count()
        self.assertEqual(old_count+1, new_count)