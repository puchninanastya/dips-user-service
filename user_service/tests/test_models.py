from django.test import TestCase

from django.contrib.auth.models import User
from user_service.models import Profile

class UserModelTestCase(TestCase):
    """This class defines the test suite for the User model."""

    def setUp(self):
        self.newUser1 = User.objects.create(username='lena001',
            first_name='Lena', last_name='Lenina',
            email='lenina@yahoo.com', password='lena007')
        self.profile1 = Profile.objects.create(user=self.newUser1,
            phone_number='+79161002030', birth_date='1995-11-10')

    def test_model_get_user(self):
        """Test the user model can get user."""
        user1 = User.objects.get(username='lena001')
        self.assertEqual(user1.first_name, 'Lena')
        self.assertEqual(user1.last_name, 'Lenina')
        self.assertEqual(user1.email, 'lenina@yahoo.com')

class ProfileModelTestCase(TestCase):
    """This class defines the test suite for the Profile model."""

    def setUp(self):
        self.newUser1 = User.objects.create(username='lena001',
            first_name='Lena', last_name='Lenina',
            email='lenina@yahoo.com', password='lena007')
        self.profile1 = Profile.objects.create(user=self.newUser1,
            phone_number='+79161002030', birth_date='1995-11-10')

    def test_model_get_profile(self):
        """Test the profile model can get profile."""
        profile1 = Profile.objects.get(pk=self.profile1.id)
        self.assertEqual(profile1.phone_number, '+79161002030')
