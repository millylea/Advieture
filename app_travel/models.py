from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(
        upload_to="tours/category", default="tours/category/default.jpg"
    )

    def __str__(self):
        return self.name


class Departure(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Tour(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="tours"
    )
    departure = models.ForeignKey(
        Departure, on_delete=models.PROTECT, related_name="dep_tours"
    )
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)
    image = models.ImageField(
        upload_to="tours/images", default="tours/images/default.png"
    )
    days = models.CharField(max_length=150)
    journey = models.CharField(max_length=200, null=True)
    transportation = models.CharField(max_length=200, null=True)
    acommondation = models.CharField(max_length=200, null=True)
    schedule = models.TextField(null=False)
    booked = models.IntegerField(default=0)
    departure_date = models.DateField(null=True)
    def children_price (self):
        return self.price/2
    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True)
    subject = models.CharField(max_length=264)
    message = models.TextField()
    created_day = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject


class Promotions(models.Model):
    name = models.CharField(max_length=250, unique=True)
    link = models.URLField(null=True)
    image = models.ImageField(
        upload_to="tours/promotions", default="tours/promotions/default.png"
    )

    def __str__(self):
        return self.name


class BackgroundSlider(models.Model):
    caption = models.CharField(max_length=250, unique=True)
    link = models.URLField(null=True)
    image = models.ImageField(
        upload_to="tours/background-slider",
        default="tours/background-slider/default.png",
    )

    def __str__(self):
        return self.caption
