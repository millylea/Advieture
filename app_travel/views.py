from django.conf import settings
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
import markdown
from datetime import datetime

from app_travel.models import (
    Category,
    Promotions,
    Tour,
    Departure,
    Contact,
)


# Create your views here.
def index(request):
    categories = Category.objects.all()
    promotions = Promotions.objects.all()

    tours = Tour.objects.all()
    departures = Departure.objects.all()
    popular_tours = tours.order_by("-booked")[0:6]
    affordable_tours = tours.order_by("price")[0:4]

    return render(
        request,
        "app_travel/index.html",
        {
            "categories": categories,
            "promotions": promotions,
            "tours": tours,
            "popular_tours": popular_tours,
            "affordable_tours": affordable_tours,
            "departures": departures,
        },
    )


def about(request):

    return render(request, "app_travel/about.html")


def tours_list(request, category_id):
    categories = Category.objects.all()
    departures = Departure.objects.all()

    tours = Tour.objects.filter(category_id=category_id)
    category_name = Category.objects.get(id=category_id).name

    p = Paginator(tours, 3)  # creating a paginator object
    page_number = request.GET.get("page")
    try:
        tours_pager = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        tours_pager = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        tours_pager = p.page(p.num_pages)
    try:
        elided_page_range = tours_pager.paginator.get_elided_page_range(
            int(page_number)
        )
        current_page = int(page_number)
    except:
        elided_page_range = tours_pager.paginator.get_elided_page_range()
        current_page = 1
    return render(
        request,
        "app_travel/tours_list.html",
        {
            "categories": categories,
            "tours": tours,
            "category_name": category_name,
            "elided_page_range": elided_page_range,
            "current_page": current_page,
            "tours_pager": tours_pager,
            "departures": departures,
        },
    )


def tour_detail(request, tour_id):
    categories = Category.objects.all()
    tour_detail = Tour.objects.filter(id=tour_id).first()
    suggested_tours = Tour.objects.filter(
        Q(category=tour_detail.category)
        & Q(departure=tour_detail.departure)
        & ~Q(id=tour_id)
    )
    md = markdown.Markdown()
    schedule_html = md.convert(tour_detail.schedule)
    return render(
        request,
        "app_travel/tour-detail.html",
        {
            "tour_detail": tour_detail,
            "schedule_html": schedule_html,
            "categories": categories,
            "suggested_tours": suggested_tours[:3],
        },
    )


def search(request):
    categories = Category.objects.all()
    departures = Departure.objects.all()
    departure_id = int(request.GET.get("departure_id"))
    category_id = int(request.GET.get("category_id"))
    departure_date = request.GET.get("departure_date")
    keyword = request.GET.get("keyword")

    tours_pager = Tour.objects.all()

    if keyword:
        tours_pager = tours_pager.filter(
            Q(name__contains=keyword)
            | Q(schedule__contains=keyword)
            | Q(journey__contains=keyword)
        )
    if departure_id:
        tours_pager = tours_pager.filter(departure=departure_id)
    if category_id:
        tours_pager = tours_pager.filter(category=category_id)
    if departure_date:
        format = "%d-%m-%Y"
        d = datetime.strptime(departure_date, format)
        tours_pager = tours_pager.filter(departure_date=d)

    count = tours_pager.count()
    if count == 1 or count > 1:
        category_name = f"Tìm thấy {count} tour"
    else:
        category_name = "Không tìm thấy tour nào"
    return render(
        request,
        "app_travel/tours_list.html",
        {
            "departure_id": departure_id,
            "category_id": category_id,
            "departure_date":departure_date,
            "categories": categories,
            "tours_pager": tours_pager,
            "category_name": category_name,
            "departures": departures,
        },
    )


def contact(request):
    categories = Category.objects.all()
    result_contact = ""
    if request.POST.get("btnGuiThongtin"):
        # gán biến
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        # Luu CSDL
        Contact.objects.create(
            name=name,
            phone=phone,
            email=email,
            subject=subject,
            message=message,
        )
        result_contact = """
             <div class="alert alert-success" role="alert">
                    Thông tin đã được ghi nhận!
             </div> """

        # Automatic Email
        sender = settings.EMAIL_HOST_USER
        recipients = [email, sender]
        title = f"[Feedback] {subject}"
        content = "<p> Chào bạn <strong>" + name + "</strong>,"
        content += (
            "<p> Advieture đã nhận được thông tin liên hệ của bạn với tiêu đề: </p>"
        )
        content += "<p>" + subject + "</p>"
        content += "<p>Chúng tôi sẽ phản hồi lại bạn trong thời gian sớm nhất.</p>"
        content += "<p>Cảm ơn bạn đã liên hệ</p>"
        msg = EmailMessage(title, content, sender, recipients)
        msg.content_subtype = "html"
        msg.send()

    return render(
        request,
        "app_travel/contact.html",
        {"result_contact": result_contact, "categories": categories},
    )
