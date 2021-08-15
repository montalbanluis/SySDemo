from .models import Persona
from rest_framework import routers, serializers, viewsets

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        exclude = ['image']

