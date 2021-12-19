from django.urls import path 
#from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('bookingform/', views.BookingFormView.as_view(), name='bookingform'),
    path('<pk>/update/', views.BookingUpdateView.as_view()),
    path('<pk>/delete/', views.BookingDeleteView.as_view()),
]