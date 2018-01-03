from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APIRequestFactory

from django.contrib.auth.models import User
from user_service.models import Profile
from user_service.serializers import UserSerializer, ProfileSerializer
from user_service.views import UserViewSet

class GetAllUsersTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()

        self.newUser1 = User.objects.create(username='lena001',
            first_name='Lena', last_name='Lenina',
            email='lenina@gmail.com', password='lena001')
        self.profile1 = Profile.objects.create(user=self.newUser1,
            phone_number='+79161002031', birth_date='1995-01-01')

        self.newUser2 = User.objects.create(username='anna002',
            first_name='Anna', last_name='Annina',
            email='anina@yahoo.com', password='anna002')
        self.profile2 = Profile.objects.create(user=self.newUser2,
            phone_number='+79161002032', birth_date='1996-02-02')

        self.newUser3 = User.objects.create(username='alena003',
            first_name='Alena', last_name='Alenina',
            email='alenina@yandex.ru', password='alena003')
        self.profile3 = Profile.objects.create(user=self.newUser3,
            phone_number='+79161002033', birth_date='1997-03-03')

    def test_get_all_users(self):
        """Test the api get valid single user."""
        # Setup.
        url = "/users/"
        request = self.factory.get(url)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        # Run.
        user_list = UserViewSet.as_view({'get': 'list'})
        response = user_list(request)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

class GetSingleUserTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()

        self.newUser1 = User.objects.create(username='lena001',
            first_name='Lena', last_name='Lenina',
            email='lenina@yahoo.com', password='lena007')
        self.profile1 = Profile.objects.create(user=self.newUser1,
            phone_number='+79161002030', birth_date='1995-11-10')

        self.invalid_pk = 2

    def test_get_valid_single_user(self):
        """Test the api get valid single user."""
        # Setup.
        url = "/users/" + str(self.newUser1.pk)
        request = self.factory.get(url)
        serializer = UserSerializer(self.newUser1)
        # Run.
        user_detail = UserViewSet.as_view({'get': 'retrieve'})
        response = user_detail(request, pk=self.newUser1.pk)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_user(self):
        """Test the api get invalid single user."""
        # Setup.
        url = "/users/" + str(self.invalid_pk)
        request = self.factory.get(url)
        # Run.
        user_detail = UserViewSet.as_view({'get': 'retrieve'})
        response = user_detail(request, pk=self.invalid_pk)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewUserTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()

        self.valid_payload = {
            "email": "angelina666@yandex.ru",
            "username": "angelina666",
            "first_name": "Angelina",
            "last_name": "Orenova",
            "password": "angelina666",
            "profile": {
                "phone_number": "+79096890709",
                "birth_date": "1994-02-15"
            }
        }

        self.invalid_payload = {
            "email": "angelina666@yandex.ru",
            "username": "",
            "first_name": "Angelina",
            "last_name": "Orenova",
            "password": "angelina666",
            "profile": {
                "phone_number": "+79096890709",
                "birth_date": "1994-02-15"
            }
        }

    def test_get_valid_single_user(self):
        """Test the api valid insert new user."""
        # Setup.
        url = "/users/"
        request = self.factory.post(url, self.valid_payload, format='json')
        # Run.
        user_list = UserViewSet.as_view({'post': 'create'})
        response = user_list(request)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_invalid_single_user(self):
        """Test the api invalid insert new user."""
        # Setup.
        url = "/users/"
        request = self.factory.post(url, self.invalid_payload, format='json')
        # Run.
        user_list = UserViewSet.as_view({'post': 'create'})
        response = user_list(request)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleUserTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()

        self.newUser1 = User.objects.create(username='lena001',
            first_name='Lena', last_name='Lenina',
            email='lenina@gmail.com', password='lena001')
        self.profile1 = Profile.objects.create(user=self.newUser1,
            phone_number='+79161002031', birth_date='1995-01-01')

        self.invalid_pk = 2

    def test_get_valid_single_user(self):
        """Test the api valid delete new user."""
        # Setup.
        url = "/users/" + str(self.newUser1.pk)
        request = self.factory.delete(url)
        # Run.
        user_detail = UserViewSet.as_view({'delete': 'destroy'})
        response = user_detail(request, pk=self.newUser1.pk)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_valid_single_user(self):
        """Test the api valid delete new user."""
        # Setup.
        url = "/users/" + str(self.invalid_pk)
        request = self.factory.delete(url)
        # Run.
        user_detail = UserViewSet.as_view({'delete': 'destroy'})
        response = user_detail(request, pk=self.invalid_pk)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
