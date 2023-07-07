# Generated by Django 4.2.2 on 2023-07-06 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SendRequest_to_login",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("surname", models.CharField(max_length=50, verbose_name="Surename")),
                ("phone_number", models.IntegerField(verbose_name="Phone Number")),
                (
                    "scanned_document",
                    models.ImageField(
                        upload_to="images_of_sc_document",
                        verbose_name="Scanned Document",
                    ),
                ),
                (
                    "activate_profile",
                    models.CharField(
                        choices=[("yes", "yes"), ("no", "no")],
                        default=0,
                        verbose_name="Activate Profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Doctor_user_Registration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phone_number", models.IntegerField(verbose_name="Phone Number")),
                (
                    "email",
                    models.EmailField(max_length=254, verbose_name="Email Address"),
                ),
                (
                    "specialization",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="Specialization"
                    ),
                ),
                (
                    "working_days",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            (0, "Monday"),
                            (1, "Tuesday"),
                            (2, "Wednesday"),
                            (3, "Thursday"),
                            (4, "Friday"),
                            (5, "Saturday"),
                            (6, "Sunday"),
                        ],
                        default="None",
                        max_length=20,
                    ),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
