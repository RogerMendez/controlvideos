from django.forms import ModelForm

from prestamo.models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo