from django.db import models
#from datetime import datetime, date

from django import template

register = template.Library()

# Create your models here.

class VehicleModel(models.Model):
    vin =  models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    modelo = models.PositiveIntegerField()
    weight = models.FloatField()