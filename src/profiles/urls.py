from django.conf.urls import url

from .views import ProfileListView
from . import views


urlpatterns = [
    url(r'^$', ProfileListView.as_view(), name='list'),
    url(r'^create/$', views.profile_create, name='create'),
    url(r'^(?P<pk>\d+)/edit/$', views.profile_edit, name='update'),
    url(r'^(?P<pk>\d+)/edit/password/$', views.admin_edit_password, name='admin_password_update'),
]
