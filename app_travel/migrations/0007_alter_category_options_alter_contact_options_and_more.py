# Generated by Django 5.0.6 on 2024-06-13 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_travel", "0006_alter_tour_schedule"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Danh Mục Tour Nội Địa"},
        ),
        migrations.AlterModelOptions(
            name="contact",
            options={"verbose_name_plural": "Liên hệ"},
        ),
        migrations.AlterModelOptions(
            name="departure",
            options={"verbose_name_plural": "Khởi Hành"},
        ),
        migrations.AlterModelOptions(
            name="promotions",
            options={"verbose_name_plural": "Ưu Đãi"},
        ),
        migrations.AlterModelOptions(
            name="tour",
            options={"verbose_name_plural": "Danh sách Tour"},
        ),
    ]