from django.contrib.auth.models import User
from .models import SendRequest_to_login, Doctor_user_Registration
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from password_generator import PasswordGenerator

pwo = PasswordGenerator()
password = pwo.generate()


@receiver(pre_save, sender=SendRequest_to_login)
def create_auth_user(sender, instance=None, created=False, **kwargs):
    if instance.activate_profile == "yes":
        username_checking = custom_checker_for_user(instance.surname)
        user = User.objects.create_user(username=username_checking, password=password)
        user.save()
        created_user = User.objects.get(username=username_checking)
        profile = Doctor_user_Registration.objects.create(
            username=created_user, phone_number=instance.phone_number
        )
        profile.save()

        print("double fired", password, instance.surname)


def custom_checker_for_user(username):
    check = User.objects.filter(username=username).exists()
    if check:
        return f"{username}_{password[0:5]}"
    return username
