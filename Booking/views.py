from django.shortcuts import render
from Booking.models import BookingModel
from Booking.forms import BookingForm
from django.views.generic import (TemplateView, 
                                    ListView, 
                                    CreateView, 
                                    FormView, 
                                    UpdateView,
                                    DeleteView)

#Create your views here.
class BookingView(ListView):
    model = BookingModel
    context_object_name = 'bookingview'
    template_name = 'Booking/booking.html'

class BookingFormView(FormView):
    # specify the Form you want to use
    form_class = BookingForm
     
    # specify name of template
    template_name = "Booking/bookingmodel_form.html"
 
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/thanks/"

    def form_valid(self, form):
        form.save()
        return super(BookingFormView, self).form_valid(form)

class BookingUpdateView(UpdateView):
    # specify the model you want to use
    model = BookingModel
 
    # specify the fields
    fields = [
        "booking_number",
        "loading_port",
        "discharge_port",
        "ship_arrival_date",
        "ship_departure_date",
    ]
 
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/"

class BookingDeleteView(DeleteView):
    # specify the model you want to use
    model = BookingModel
     
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url ="/"