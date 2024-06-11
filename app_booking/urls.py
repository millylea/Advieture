from django.urls import path
from app_booking.views import *

# Create your views here.


app_name = "app_booking"
urlpatterns = [
    path("dat-tour/<int:tour_id>/", tour_booking, name="tour_booking"),
    path("tien-hanh-dat/<int:booking_id>/", checkout, name="checkout"),
   
]
