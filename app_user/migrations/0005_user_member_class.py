# Generated by Django 5.0.6 on 2024-06-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_user", "0004_alter_user_email_alter_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="member_class",
            field=models.CharField(max_length=150, null=True),
        ),
    ]
