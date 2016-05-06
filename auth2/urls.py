# coding: utf-8
from django.conf.urls import url

from auth2 import views


urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
]
