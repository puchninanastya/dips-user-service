from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class UserToken(models.Model):
    token = models.CharField(max_length=30, null=True)
    expires = models.DateTimeField(null=True)
    user = models.OneToOneField(User,
        related_name='auth_token', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "User Token"
        verbose_name_plural = "User Tokens"

    def __str__(self):
        return "Toker for user {} is {}".format(self.user, self.token)

class AppToken(models.Model):
    client_id = models.CharField(max_length=40)
    client_secret = models.CharField(max_length=128)
    token = models.CharField(max_length=30, blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "App Token"
        verbose_name_plural = "App Tokens"

    def __str__(self):
        return "Toker for cliend id {} is {}".format(self.client_id, self.token)

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
        verbose_name="Birthdate")
    height = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(200), MinValueValidator(140)],
        verbose_name="Height")
    bust = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(110), MinValueValidator(40)],
        verbose_name="Bust (shape measurement)")
    waist = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(110), MinValueValidator(40)],
        verbose_name="Waist (shape measurement)")
    hips = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(110), MinValueValidator(40)],
        verbose_name="Hips (shape measurement)")
    shoe = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(45), MinValueValidator(30)],
        verbose_name="Shoe (shape measurement)")
    eyes = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        verbose_name="Eyes color")
    hair = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        verbose_name="Hair color")

    class Meta:
        verbose_name = "User profile"
        verbose_name_plural = "User profiles"

    def __str__(self):
        return "{}".format(self.user.username)
