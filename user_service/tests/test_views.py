from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from user_service.models import Profile

'''
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        # TODO: add user data
        self.userprofile_data = {'username': 'new007',
            'password': 'newpass111',
            'first_name': 'Newer',
            'last_name': 'Novii',
            'email': 'newer007@gmail.com',
            'phone_number': '+79160980809' }
        self.userprofile_data = {}
        self.response = self.client.post(
            reverse('users'),
            self.userprofile_data,
            format="json")

    def test_api_can_create_a_profile(self):
        """Test the api has profile creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
'''
