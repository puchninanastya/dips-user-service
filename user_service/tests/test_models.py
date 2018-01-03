from django.test import TestCase

from django.contrib.auth.models import User
from user_service.models import Profile

class ModelTestCase(TestCase):
    """This class defines the test suite for the Profile model."""

    def setUp(self):
        self.newUser1 = User.objects.create(username='lena001',
            first_name='Lena', last_name='Lenina',
            email='lenina@yahoo.com', password='lena007')
        self.profile1 = Profile.objects.create(user=self.newUser1,
            phone_number='+79161002030', birth_date='1995-11-10')
        self.newUser2 = User.objects.create_user(username='vasss',
            first_name='Vasilisa', last_name='Pupkina',
            email='vasss@gmail.com', password='vasss')
        self.profile2 = Profile(user=self.newUser2,
            phone_number='+79094005060', birth_date='1993-10-12')
        self.newUser3 = User.objects.create_user(username='omega',
            first_name='Olga', last_name='Silomonova',
            email='omega@yahoo.com', password='asdfg9090')
        self.profile3 = Profile(user=self.newUser3,
            phone_number='+79094005060', birth_date='1998-12-05')
        self.newUser4 = User.objects.create_user(username='anna21',
            first_name='Anna', last_name='Ivanova',
            email='anna21@yandex.ru', password='anna21')
        self.profile4 = Profile(user=self.newUser4,
            phone_number='+79151005060', birth_date='1997-02-10')

    def test_model_can_create_profile(self):
        """Test the profile model can create Profiles."""
        old_count = Profile.objects.count()
        self.profile2.save()
        self.profile3.save()
        self.profile4.save()
        new_count = Profile.objects.count()
        self.assertEqual(old_count+3, new_count)

    def test_model_get_user(self):
        """Test the user model can get user."""
        user1 = User.objects.get(username='lena001')
        self.assertEqual(user1.first_name, 'Lena')
        self.assertEqual(user1.last_name, 'Lenina')
        self.assertEqual(user1.email, 'lenina@yahoo.com')

    def test_model_get_profile(self):
        """Test the profile model can get profile."""
        profile1 = Profile.objects.get(pk=self.profile1.id)
        self.assertEqual(profile1.phone_number, '+79161002030')
