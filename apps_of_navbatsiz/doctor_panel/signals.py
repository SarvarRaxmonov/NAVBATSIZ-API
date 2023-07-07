from django.contrib.auth.models import User
from .models import SendRequest_to_login, Doctor_user_Registration
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from password_generator import PasswordGenerator

pwo = PasswordGenerator()
password = pwo.generate()


@receiver(pre_save, sender=SendRequest_to_login)
def create_auth_user(sender, instance=None, created=False, **kwargs):
    if instance.activate_profile == "yes":
        username_checking = custom_username_checker(instance.surname)
        if username_checking:
            instance.surname = custom_username_maker(instance.surname)
        user = User.objects.create_user(username=instance.surname, password=password)
        user.save()
        user_created = User.objects.get(id=user.id)
        profile = Doctor_user_Registration.objects.create(
            username=user_created, phone_number=instance.phone_number
        )
        profile.save()
@receiver(pre_delete, sender=User)
def delete_user(sender, instance, **kwargs):
        profile = Doctor_user_Registration.objects.filter(username=instance.id)
        if profile.exists():
            profile.delete()
        return instance


def custom_username_checker(username):
    check = User.objects.filter(username=username).exists()
    return check
def custom_username_maker(username):
    return f"{username}_{password[0:5]}"





