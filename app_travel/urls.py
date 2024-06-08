from django.urls import path
from app_travel.views import *

app_name = "app_travel"

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("tours_list/<int:category_id>/", tours_list, name="tours_list"),
    path("tour/<int:tour_id>/", tour_detail, name="tour_detail"),
    path("search/", search, name="search"),
    path("lien-he/", contact, name="contact"),
]
