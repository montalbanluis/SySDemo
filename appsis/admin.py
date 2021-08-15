from django.contrib import admin
from .models import Persona

# Register your models here.

admin.site.register(Persona)




# CONFIGURAR EL TITULO DEL PANEL

title = "Master en Python"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de Gestión"
