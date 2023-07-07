# Generated by Django 4.2.2 on 2023-07-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctor_panel", "0003_remove_doctor_user_registration_working_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor_user_registration",
            name="working_time",
            field=models.JSONField(default={}, verbose_name="Working Time"),
        ),
    ]
