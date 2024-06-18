from django.contrib import admin
from app_user.models import *
from django.utils.html import format_html
from datetime import datetime


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "alt_last_name",
        "alt_first_name",
        "alt_phone",
        "email",
        "alt_member_class",
    ]

    @admin.display(description="Họ")
    def alt_last_name(self, obj):
        return obj.last_name

    @admin.display(description="Tên")
    def alt_first_name(self, obj):
        return obj.first_name

    @admin.display(description="Số Điện Thoại")
    def alt_phone(self, obj):
        return obj.phone

    @admin.display(description="Thành Viên")
    def alt_member_class(self, obj):
        return obj.member_class


# Register your models here.
admin.site.register(User, UserAdmin)
