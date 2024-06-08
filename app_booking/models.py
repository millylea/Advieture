from django.db import models
from app_travel.models import Tour
from app_user.models import User


class BookingStatus(models.TextChoices):
    DRAFT = "D"
    PAID = "P"
    COMPLETE = "C"


# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1, choices=BookingStatus.choices, default=BookingStatus.DRAFT
    )
    created_date = models.DateTimeField(auto_now_add=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    adult_quantity = models.IntegerField(default=1)
    children_quantity = models.IntegerField(default=0)
    discount = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    class Meta:
        ordering = ("-created_date",)

    def __str__(self):
        return f"#{self.id}"


class BookingHistory(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

