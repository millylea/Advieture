# Generated by Django 5.0.6 on 2024-06-13 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_booking", "0007_rename_bookinghistory_bookingmanager_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bookingmanager",
            name="user",
        ),
    ]
