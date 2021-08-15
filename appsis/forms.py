from django import forms
from .models import Persona
from django.core.exceptions import ValidationError

class PersonaModeloForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'


