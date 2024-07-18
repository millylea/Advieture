from django.urls import path
from app_travel.views import *

app_name = "app_travel"

urlpatterns = [
    path("", index, name="index"),
    path("Danh-sach-tour/<int:category_id>", tours_list, name="tours_list"),
    path("tour/<int:tour_id>", tour_detail, name="tour_detail"),
    path("tim-kiem/", search, name="search"),
    path("lien-he", contact, name="contact"),
]
