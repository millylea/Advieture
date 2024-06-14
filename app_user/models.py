from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(
        max_length=100, unique=True, error_messages={"unique": "Tên dăng nhập đã tồn tại."}
    )
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(
        null=True,
        blank=True,
        unique=True,
        error_messages={"unique": "Email đã tồn tại."},
    )
    address = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=250)
    member_class = models.CharField(max_length=150, default="Hạng Đồng")

    def __str__(self) -> str:
        return self.username
