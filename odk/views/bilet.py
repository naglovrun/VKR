# -*- coding: utf8 -*-
from django.shortcuts import render
from odk.forms import ClientForm
from odk.models import Client, Bilet, Zaly


def get_bilet(request, nomer):
    bilet = Bilet.objects.get(id=nomer)
    return render(request, 'odk/bilet.html', {'bilet': bilet})


def bilets_from_client(request, client_id):
    context = {}
    client = Client.objects.get(id=client_id)
    context['client'] = client
    print(client.id)

    bilets = client.bilets.all()
    context['bilets'] = bilets

    return render(request, 'odk/bilets_from_client.html', context)

