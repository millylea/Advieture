from django.urls import path
from app_API.views import *
app_name = "app_API"

urlpatterns = [
    path("domestic-tours/", domestic_tours, name="domestic_tours"),
]
