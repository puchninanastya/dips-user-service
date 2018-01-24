from django.contrib import admin
from .models import Profile, UserToken, AppToken

admin.site.register(Profile)
admin.site.register(UserToken)
admin.site.register(AppToken)
