from django.shortcuts import render
from Vehicle.models import VehicleModel
from django.views.generic import (TemplateView, ListView)

#Create your views here.
class VehicleView(ListView):
    model = VehicleModel
    context_object_name = 'vehicleview'
    template_name = 'Vehicle/vehicle.html'