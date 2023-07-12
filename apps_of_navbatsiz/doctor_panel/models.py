from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from .choices import Activate_choices, Doctor_specialties
from django.contrib.postgres.fields import ArrayField


class Doctor_Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(verbose_name="Phone Number", null=False)
    email = models.EmailField(verbose_name="Email Address")
    specialization = models.CharField(
        verbose_name="Specialization",
        choices=Doctor_specialties,
        max_length=120,
        blank=True,
    )
    sub_specializations = MultiSelectField(
        choices=Doctor_specialties, max_length=120, blank=True
    )
    working_schedule = ArrayField(
        ArrayField(models.CharField(max_length=100, blank=True), size=10, default=list),
        size=10,
        default=list,
    )
    study_description = models.CharField(max_length=1000, default=".")
    experience = models.IntegerField(null=False, default=0)
    additional_description = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.username.username



# ----------------------------------------------------------------

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


