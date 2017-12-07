from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    phone_regex = RegexValidator(regex=r'^\++[7]+\d{10}$', message="Phone number must be entered in the format: '+79999999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True)
