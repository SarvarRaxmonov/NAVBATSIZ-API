# Generated by Django 4.2.1 on 2023-07-11 02:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("doctor_panel", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doctor_profile",
            name="specialization",
        ),
    ]
