# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-24 23:24
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=40)),
                ('client_secret', models.CharField(max_length=128)),
                ('token', models.CharField(max_length=30, null=True)),
                ('expires', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, default='', max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+79999999999'.", regex='^\\++[7]+\\d{10}$')], verbose_name='Phone number')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birthdate')),
                ('height', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(140)], verbose_name='Height')),
                ('bust', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(110), django.core.validators.MinValueValidator(40)], verbose_name='Bust (shape measurement)')),
                ('waist', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(110), django.core.validators.MinValueValidator(40)], verbose_name='Waist (shape measurement)')),
                ('hips', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(110), django.core.validators.MinValueValidator(40)], verbose_name='Hips (shape measurement)')),
                ('shoe', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(45), django.core.validators.MinValueValidator(30)], verbose_name='Shoe (shape measurement)')),
                ('eyes', models.CharField(blank=True, max_length=30, null=True, verbose_name='Eyes color')),
                ('hair', models.CharField(blank=True, max_length=30, null=True, verbose_name='Hair color')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User profile',
                'verbose_name_plural': 'User profiles',
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=30, null=True)),
                ('expires', models.DateTimeField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_token', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
            },
        ),
    ]
