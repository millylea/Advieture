from django.contrib import admin
from app_travel.models import *
from django.utils.html import format_html
from datetime import datetime


class TourAdmin(admin.ModelAdmin):
    # list_display = ["name", "price", "days","departure_date", "booked"]
    list_display = [
        "alt_name",
        "alt_price",
        "alt_days",
        "alt_departure_date",
        "alt_booked",
    ]

    @admin.display(description="Tên Tour")
    def alt_name(self, obj):
        return obj.name

    @admin.display(description="Giá tour/Người lớn") 
    def alt_price(self, obj):
        return '{:,}'.format(int(obj.price))

    @admin.display(description="Số Ngày Đi") 
    def alt_days(self, obj):
        return obj.days

    @admin.display(description="ngày Khởi Hành") 
    def alt_departure_date(self, obj):
        return obj.departure_date

    @admin.display(description="Lượt Khách Đặt") 
    def alt_booked(self, obj):
        return obj.booked


# Register your models here.
admin.site.register(Category)
admin.site.register(Tour, TourAdmin)
admin.site.register(Departure)
admin.site.register(Promotions)
admin.site.register(Contact)

admin.site.site_header = "Quản Trị Advieture"
