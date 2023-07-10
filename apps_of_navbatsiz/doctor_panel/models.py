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
Activate_choices = (
    ("yes", "yes"),
    ("no", "no"),
)


class Doctor_user_Registration(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(verbose_name="Phone Number", null=False)
    email = models.EmailField(verbose_name="Email Address")
    specialization = models.CharField(
        verbose_name="Specialization", max_length=50, blank=True
    )
    working_schedule = models.JSONField(verbose_name="Working Schedule", default=dict)


class SendRequest_to_login(models.Model):
    surname = models.CharField(verbose_name="Surename", max_length=50)
    phone_number = models.IntegerField(verbose_name="Phone Number", null=False)
    email = models.EmailField(default="example@gmail.com", verbose_name="Email Address")
    scanned_document = models.ImageField(
        verbose_name="Scanned Document", upload_to="images_of_sc_document", blank=False
    )
    activate_profile = models.CharField(
        verbose_name="Activate Profile",
        choices=Activate_choices,
        default=0,
    )
