# Generated by Django 5.0.6 on 2024-06-13 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_booking", "0008_remove_bookingmanager_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="discount",
            field=models.IntegerField(default=0),
        ),
    ]
