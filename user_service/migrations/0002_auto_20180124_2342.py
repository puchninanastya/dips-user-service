# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-24 23:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apptoken',
            options={'verbose_name': 'AppToken', 'verbose_name_plural': 'AppTokens'},
        ),
        migrations.AlterModelOptions(
            name='usertoken',
            options={'verbose_name': 'UserToken', 'verbose_name_plural': 'UserTokens'},
        ),
    ]
