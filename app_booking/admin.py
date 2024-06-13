from django.contrib import admin
from app_booking.models import *
from django.utils.html import format_html
from datetime import datetime

# Customize Admin


# Register your models here.
admin.site.register(Booking)
admin.site.register(Passenger)
