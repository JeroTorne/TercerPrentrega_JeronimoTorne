from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
        path('inicio/', index, name="inicio"),
        path('pacientes/', pacientes, name="pacientes"),
        path('consultas/', consultas, name="consultas"),
        path('turnos/', turnos, name="turnos"),
        path('pacientesbd/', pacientesbd, name="pacientesbd"),

        path("buscarpaciente/",buscarpaciente, name="buscarpaciente"),
        path("buscar2/", buscar2, name="buscar2")
    ]
