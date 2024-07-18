from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from app_travel.models import Category, Tour, Contact, Departure
from app_user.models import User
from app_booking.models import Booking, BookingStatus, Passenger
from app_user.views import *


@csrf_exempt
def tour_booking(request, tour_id):
    categories = Category.objects.all()
    tour_detail = Tour.objects.get(id=tour_id)
    user_id = request.session.get("s_user")["id"]
    user = User.objects.get(pk=user_id)

    if request.POST.get("btnCheckout"):
        try:
            adult_quantity = request.POST.get("adult_quantity")
            children_quantity = request.POST.get("children_quantity")
            discount = int(request.POST.get("discount"))

            if not adult_quantity.isdigit() or not children_quantity.isdigit():
                raise ValueError("Nhập số lượng là số")
            adult_quantity = int(adult_quantity)
            children_quantity = int(children_quantity)
            if adult_quantity < 1:
                raise ValueError("Số lượng Người Lớn ít nhất là 1 ")
            if children_quantity < 0:
                raise ValueError("Số lượng phải là số dương")
        except ValueError as err:
            return render(
                request, "app_travel/booking.html", {"error": f"{err}"}, status=400
            )

        booking = Booking(
            user=user,
            tour=tour_detail,
            adult_quantity=adult_quantity,
            children_quantity=children_quantity,
            discount=discount,
        )
        booking.total_price = (
            booking.adult_total_price
            + booking.children_total_price
            - booking.discount_price
        )
        booking.save()
        name = request.POST.get("p_name")
        phone = request.POST.get("p_phone")
        address = request.POST.get("p_address")
        passenger = Passenger(name=name,phone=phone, address=address, booking=booking)
        passenger.save()
        return redirect("app_booking:checkout", booking.id)

    return render(
        request,
        "app_travel/booking.html",
        {"categories": categories, "tour_detail": tour_detail},
    )

@csrf_exempt
def checkout(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    passenger_price = booking.adult_total_price + booking.children_total_price
    print(booking.children_total_price)

    if request.POST.get("btnPayment"):
        booking.status = BookingStatus.PAID
        booking.tour.booked += 1
        booking.save()

        email = booking.user.email
        name = booking.user.last_name + " " + booking.user.first_name
        tour = booking.tour.name
        payment = "{:,}".format(booking.total_price)
        # Automatic Email
        sender = settings.EMAIL_HOST_USER
        recipients = [email, sender]
        title = f"[Thông báo] {booking.id}"
        content = "<p> Chào bạn <strong>" + name + "</strong>,"
        content += f"<p> Advieture xác nhận hoàn tất thanh toán số tiền {payment} cho chuyến đi: </p>"
        content += f"<p> {tour} </p>"
        content += "<p>Cảm ơn bạn đã tin tưởng Advieture</p>"
        msg = EmailMessage(title, content, sender, recipients)
        msg.content_subtype = "html"
        msg.send()
        return redirect("app_user:my_account")

    return render(
        request,
        "app_travel/check-out.html",
        {"booking": booking, "passenger_price": passenger_price},
    )
