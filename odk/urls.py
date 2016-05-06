# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('odk.views',
    url(r'^client/list/$', 'client.list_clients'),
    url(r'^client/(\d+)/$', 'client.get_client'),
    url(r'^client/from_bilet/(\d+)/$', 'client.client_from_bilet'),
    url(r'^client/create/$', 'client.create'),

    url(r'^bilet/(\d+)/$', 'bilet.get_bilet'),
    url(r'^bilets_from_client/(\d+)/$', 'bilet.bilets_from_client'),
)

