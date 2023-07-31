from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index (request):
    return render(request,"aplicacion/base.html")

def pacientes (request):
    return render (request, "aplicacion/pacientes.html")

def pacientesbd (request):
    return render (request, "aplicacion/pacientesbd.html")

def consultas (request):
    return render (request, "aplicacion/consultas.html")

def turnos (request):
    return render (request, "aplicacion/turnos.html")

#Registro usuario

def formPacientes (request):
    if request.method=="POST":
        paciente = paciente(nombre=request.POST ['nombre'], apellido=request.POST['apellido'], telefono=request.POST['telefono'] )
        paciente.save()
        return HttpResponse ('Paciente creado con éxito')
    return render (request, "aplicacion/pacientes.html")

def pacientesbd (request):
    ctx = {"paciente" : Paciente.objects.all()}
    return render(request, "aplicacion/pacientesbd.html", ctx)

def buscarpaciente(request):
    return render (request, "aplicacion/buscarpaciente.html")

def buscar2(request):
    if request.GET["paciente"]:
        paciente = request.GET["paciente"]
        busqueda = Paciente.objects.filter(nombre__icontains=paciente)
        return render(request, "aplicacion/resultadopaciente.html",{"Paciente" : paciente})
    return HttpResponse ("No se encuentra el paciente solicitado")