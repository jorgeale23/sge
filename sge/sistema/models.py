# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.validators import RegexValidator

import time

# Create your models here.
class Linea(models.Model):
    Nombre = models.CharField(max_length=35)

    def __str__(self) :
        return self.Nombre



class Electrodomestico(models.Model):
    Nombre = models.CharField(max_length=35)
    Marca = models.CharField(max_length=35, blank=True)
    Modelo = models.CharField(max_length=35, blank=True)
    Horas = models.FloatField()
    Activo = models.BooleanField(default=True)
    Consumo = models.FloatField()
    Clima = (('F', 'Frio'), ('C', 'Calor'), ('M', 'Mixto'))
    TipoClima = models.CharField(max_length=1, choices=Clima, blank=True)
    Linea = models.ForeignKey(Linea, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self) :
        return self.Nombre


class Ajuste(models.Model):
    Habitantes = models.PositiveIntegerField()
    Politica = models.PositiveIntegerField()
    Hemisferio = models.CharField(max_length=1)
    #NomLinea1 = models.CharField(max_length=35)
    #NomLinea2 = models.CharField(max_length=35)
    #NomLinea3 = models.CharField(max_length=35)


class Medicion(models.Model):
    FyHinicio = models.DateField()
    FyHfin = models.DateField()
    Tension = models.FloatField()
    Corriente = models.FloatField()
    Potencia = models.FloatField()
    FactorPotencia = models.FloatField()
    Linea = models.PositiveIntegerField()

class HoraLuz(models.Model):
    Mes = models.PositiveIntegerField()
    Amanecer = models.TimeField()
    PuestaSol = models.TimeField()
    def __str__(self) :
        return str(self.Mes)


class HoraCasa(models.Model):
    Dias = (('1', 'Lunes'), ('2', 'Martes'), ('3', 'Miercoles'), ('4', 'Jueves'), ('5', 'Viernes'), ('6', 'Sabado'), ('7', 'Domingo'))
    Dia = models.CharField(max_length=1, choices=Dias)
    Inicio = models.TimeField()
    Fin = models.TimeField()
    def __str__(self) :
        return str(self.Dia)
