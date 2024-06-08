from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.mail import EmailMessage
from datetime import datetime
from app_travel.models import Category, Tour, Contact
from app_user.models import User
from app_booking.models import Booking
from app_user.views import *


def tour_booking(request, tour_id):
    categories = Category.objects.all()
    tour_detail = Tour.objects.filter(id=tour_id).first()

    user = request.session.get("s_user")

    if request.POST.get("btnCheckout"):
        try:

            adult_quantity = int(request.POST.get("adult_quantity"))
            children_quantity = int(request.POST.get("children_quantity"))

        except ValueError:
            return render(
                request, "app_travel/booking.html", {"error": "error"}, status=400
            )

        booking_price = (adult_quantity + children_quantity) * tour_detail.price
        booking = Booking(
            user["id"],
            tour=tour_detail,
            total_price=booking_price,
            adult_quantity=adult_quantity,
            children_quantity=children_quantity,
        )
        booking.save()
        return redirect("app_booking:checkout")
    return render(
        request,
        "app_travel/booking.html",
        {"categories": categories, "tour_detail": tour_detail},
    )


def checkout(request):

    return render(request, "app_travel/check-out.html")
