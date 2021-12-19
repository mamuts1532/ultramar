from django.db import models
#from datetime import datetime, date

from django import template

register = template.Library()

# Create your models here.

class BookingModel(models.Model):
    booking_number =  models.PositiveIntegerField(unique=True)
    loading_port = models.PositiveIntegerField()
    discharge_port = models.PositiveIntegerField()
    ship_arrival_date = models.DateField(editable=True, blank=True)
    ship_departure_date = models.DateField(editable=True, blank=True)