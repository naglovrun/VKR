from django import forms
from odk.models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('familiya', 'imya', 'vozrast')


class ClientFilterForm(forms.Form):
    familiya = forms.CharField(required=False)
    imya = forms.CharField(required=False)
    vozrast = forms.IntegerField(required=False)
