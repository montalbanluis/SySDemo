from django.shortcuts import render
from .models import Persona
from rest_framework import viewsets
from .serializers import PersonaSerializer

# Create your views here.

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

