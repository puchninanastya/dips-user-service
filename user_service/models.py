from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(
        regex=r'^\++[7]+\d{10}$',
        message="Phone number must be entered in the format: '+79999999999'."
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=12,
        blank=True,
        default='',
        verbose_name="Phone number")
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name= "Birthdate")

    class Meta:
        verbose_name = "User profile"
        verbose_name_plural = "User profiles"

    def __str__(self):
        return "{}".format(self.user.username)
