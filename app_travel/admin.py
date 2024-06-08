from django.contrib import admin
from app_travel.models import *
from django.utils.html import format_html
from datetime import datetime

# Register your models here.
admin.site.register(Category)
admin.site.register(Tour)
admin.site.register(Departure)
admin.site.register(Promotions)

admin.site.site_header = "Quản Trị Advieture"
