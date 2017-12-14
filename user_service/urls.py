from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<id>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^profiles/$', views.ProfileList.as_view(), name='profile-list'),
    url(r'^profiles/(?P<id>[0-9]+)/$', views.ProfileDetail.as_view(), name='profile-detail'),
]
