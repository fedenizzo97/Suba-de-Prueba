from django import http
from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader

def saludo(request):
    return HttpResponse("Hola Django")

def segundaVista(request):
    return HttpResponse("Segunda Vista")

def miNombreES(self,nombre):

    documentoDeTexto= f"Mi nombre es: <br><br> {nombre}"
    return  HttpResponse(documentoDeTexto)

def probandoTemplate(self):

    nombre= "Fede"
    apellido= "Nizzo"
    diccionario= {"nombre":nombre,"apellido": apellido}

    plantilla= loader.get_template("template1.html")
  
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)