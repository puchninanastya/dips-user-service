from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.ProfileViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^user-auth-token/check$', views.UserTokenCheckView.as_view(), name='check-user-token'),
    url(r'^user-auth-token/$', views.UserTokenView.as_view(), name='create-user-token'),
    url(r'^app-auth-token/$', views.AppTokenView.as_view(), name='create-app-token'),
]
