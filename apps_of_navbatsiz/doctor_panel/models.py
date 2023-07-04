from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


DAYS_OF_WEEK = (
    (0, "Monday"),
    (1, "Tuesday"),
    (2, "Wednesday"),
    (3, "Thursday"),
    (4, "Friday"),
    (5, "Saturday"),
    (6, "Sunday"),
)


class Doctor_user_Registration(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.IntegerField(verbose_name="Password", null=False)
    phone_number = models.IntegerField(verbose_name="Phone Number", null=False)
    email = models.EmailField(verbose_name="Email Address")
    specialization = models.CharField(verbose_name="Specialization", max_length=50)
    working_time = models.TimeField(verbose_name="Working Time", null=False)
    working_days = MultiSelectField(
        choices=DAYS_OF_WEEK, max_choices=6, max_length=20, default="None"
    )


class SendRequest_to_login(models.Model):
    surname = models.CharField(verbose_name="Surename", max_length=50)
    phone_number = models.IntegerField(verbose_name="Phone Number", null=False)
    scanned_document = models.ImageField(
        verbose_name="Scanned Document", upload_to="images_of_sc_document", blank=False
    )
    activate_profile = models.CharField(
        verbose_name="Activate Profile",
        max_length=50,
        choices=((1, "yes"), (2, "no")),
        default=0,
    )
