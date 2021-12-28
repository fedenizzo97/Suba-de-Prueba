from django.db import models
# Create your models here.

class Guantes(models.Model):
    marca= models.CharField(max_length=40)
    tamanio= models.CharField(max_length=20)
    precio= models.IntegerField()

class Barbijos(models.Model):
    marca= models.CharField(max_length=40)
    tamanio= models.CharField(max_length=20)
    precio= models.IntegerField()

class Oximetros(models.Model):
    marca= models.CharField(max_length=40)
    origen= models.CharField(max_length=40)
    precio= models.IntegerField()