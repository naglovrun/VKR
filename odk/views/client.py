# -*- coding: utf8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render
from odk.forms import ClientForm, ClientFilterForm
from odk.models import Client, Bilet, Zaly


#views - представления, контроллеры - способ передачи в хтмль наших данных
def list_clients(request):
    c = {}
    clients = Client.objects.all()
    form = ClientFilterForm(request.GET or None)
    if form.is_valid():
        if form.cleaned_data.get('familiya'):
            clients = clients.filter(familiya__icontains=form.cleaned_data['familiya'])

    #template_name - имя шаблон т.е. хьмль
    c['clients'] = clients
    c['form'] = form
    return render(request, 'odk/client/list_clients.html', c)


def get_client(request, nomer):
    client = Client.objects.get(id=nomer)
    return render(request, 'odk/client/get_client.html', {'client': client})


def client_from_bilet(request, bilet_id):
    context =  {}
    bilet = Bilet.objects.get(id=bilet_id)
    context['bilet'] = bilet
    print(bilet.id)

    client = bilet.сlient
    print(client.id)
    context['client'] = client
    return render(request, 'odk/client/client_from_bilet.html', context)


def create(request):
    c = {}
    form = ClientForm(request.GET or None)
    if form.is_valid():
        form.save()
        return reverse('odk.view.client.list_clients')

    print(form)
    c['form'] = form
    return render(request, 'odk/client/create.html', c)