from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.mail import EmailMessage
from datetime import datetime
from app_travel.models import Category, Tour, Contact, Departure
from app_user.models import User
from app_booking.models import Booking, BookingStatus
from app_user.views import *


def tour_booking(request, tour_id):
    categories = Category.objects.all()
    tour_detail = Tour.objects.get(id=tour_id)

    user_id = request.session.get("s_user")["id"]
    user = User.objects.get(pk=user_id)
    if request.POST.get("btnCheckout"):
        try:

            adult_quantity = int(request.POST.get("adult_quantity"))
            children_quantity = int(request.POST.get("children_quantity"))

        except ValueError:
            return render(
                request, "app_travel/booking.html", {"error": "error"}, status=400
            )
        
        booking = Booking(
            user=user,
            tour=tour_detail,
            adult_quantity=adult_quantity,
            children_quantity=children_quantity,
        )
        booking.total_price = booking.adult_price(
            tour_detail.price
        ) + booking.children_price(tour_detail.price)
        booking.save() - booking.discount
        return redirect("app_booking:checkout")
    return render(
        request,
        "app_travel/booking.html",
        {"categories": categories, "tour_detail": tour_detail},
    )


def checkout(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.POST.get("btnPayment"):
        booking.status = BookingStatus.PAID
        booking.save()
        return redirect("app_user:my_account")

    return render(
        request,
        "app_travel/check-out.html",
        {
            "booking": booking,
        },
    )


def result(request, booking_id):
    booking = Booking.objects.get(id=booking_id)

    return render(
        request,
        "app_travel/result.html",
        {
            "booking": booking,
        },
    )
