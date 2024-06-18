from django.contrib import admin
from app_booking.models import *
from django.db.models import Q
from django.utils.html import format_html
from datetime import datetime

# Customize Admin

def change_status(modeladmin, request,queryset):
    queryset.update(status="C")

change_status.short_description = "Cập nhật hoàn thành tour"

class BookingAdmin(admin.ModelAdmin):
    list_display = [
        "alt_id",
        "alt_tour",
        "alt_departure_date",
        "alt_status",
        "alt_user",
        "alt_adult_quantity",
        "alt_children_quantity",
    ]
    exclude = ["total_price", "discount"]
    list_filter = ["tour__departure_date","status"]
    search_fields = ["tour__contains"]
    actions = [change_status]

    @admin.display(description="Mã Booking")
    def alt_id(self, obj):
        return f"#{obj.id}"

    @admin.display(description="Tên Tour")
    def alt_tour(self, obj):
        return obj.tour

    @admin.display(description="Ngày Khởi Hành")
    def alt_departure_date(self, obj):
        return obj.tour.departure_date.strftime("%d-%m-%Y")

    @admin.display(description="Trạng Thái")
    def alt_status(self, obj):
        return obj.status

    @admin.display(description="Người Đặt")
    def alt_user(self, obj):
        return obj.user

    @admin.display(description="Người Lớn")
    def alt_adult_quantity(self, obj):
        return obj.adult_quantity

    @admin.display(description="Trẻ Em")
    def alt_children_quantity(self, obj):

        return obj.children_quantity


# Register your models here.
admin.site.register(Booking, BookingAdmin)
admin.site.register(Passenger)
