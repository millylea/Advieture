from django.urls import path
from app_user.views import *

app_name = "app_user"

urlpatterns = [
    path("tao-tai-khoan", register, name="register"),
    path("dang-nhap", login, name="login"),
    path("dang-xuat", logout, name="logout"),
    path("tai-khoan-cua-toi", my_account, name="my_account"),
   
    path(
        "xuat-hoa-don/<int:booking_id>",
        export_payment_to_pdf,
        name="export_payment_to_pdf",
    ),
]
