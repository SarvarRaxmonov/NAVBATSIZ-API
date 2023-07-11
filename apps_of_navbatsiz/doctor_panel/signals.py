from django.contrib.auth.models import User
from .models import SendRequest_to_login, Doctor_Profile
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from password_generator import PasswordGenerator
from django.core.mail import send_mail
from django.conf import settings

pwo = PasswordGenerator()
password = pwo.generate()


@receiver(pre_save, sender=SendRequest_to_login)
def create_auth_user(sender, instance=None, created=False, **kwargs):
    if instance.activate_profile == "yes":
        username_checking = custom_username_checker(instance.surname)
        if username_checking:
            instance.surname = custom_username_maker(instance)
        user = User.objects.create_user(username=instance.surname, password=password)
        user.save()
        create_profile(user, instance)
    return instance


def create_profile(user: object, instance: object):
    user_created = User.objects.get(id=user.id)
    profile = Doctor_Profile.objects.create(
        username=user_created, phone_number=instance.phone_number, email=instance.email
    ).save()
    send_verification_to_user_email(instance.email, instance.surname, password)


@receiver(pre_delete, sender=User)
def delete_user(sender, instance, **kwargs):
    profile = Doctor_Profile.objects.filter(username=instance.id)
    if profile.exists():
        profile.delete()
    return instance


def send_verification_to_user_email(email, username, password):
    return send_mail(
        "Verification Code from Navbatsiz",
        f"Your verification code is {password} and your username {username} you can login into your account "
        + "by visiting our site at https://navbatsiz.com/login",
        "settings.EMAIL_HOST_USER",
        [email],
        fail_silently=False,
    )


def custom_username_checker(username):
    check = User.objects.filter(username=username).exists()
    return check


def custom_username_maker(instance):
    return f"{instance.surname}_{str(instance.phone_number)[2:9]}"
