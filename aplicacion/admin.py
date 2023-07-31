from django.contrib import admin
from .models import Paciente, Turnos, Consultas
# Register your models here.

admin.site.register(Paciente)
admin.site.register(Turnos)
admin.site.register(Consultas)