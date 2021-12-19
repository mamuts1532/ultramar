from django import forms
from .models import BookingModel
 
 
# creating a form
class BookingForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = BookingModel
 
        # specify fields to be used
        fields = [
            "booking_number",
            "loading_port",
            "discharge_port",
            "ship_arrival_date",
            "ship_departure_date",
        ]