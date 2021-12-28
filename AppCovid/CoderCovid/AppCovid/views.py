from django.shortcuts import render, HttpResponse

from django.http import HttpResponse

from AppCovid.models import Guantes,Barbijos,Oximetros
# Create your views here.
def inicio(request):

    return render(request, "AppCovid/inicio.html")

def Guantes(request):
    return render(request, "AppCovid/guantes.html")


def Barbijos(request):
    return render(request, "AppCovid/barbijos.html")

def Oximetros(request):
    return render(request, "AppCovid/oximetros.html")