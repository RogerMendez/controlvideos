from django.forms import ModelForm
from django import forms

from ventas.models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente