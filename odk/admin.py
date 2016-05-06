from django.contrib import admin
from .models import Client, Bilet, Zaly


# class AdminClient():

admin.site.register(Client)
admin.site.register(Bilet)
admin.site.register(Zaly)