from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.username
