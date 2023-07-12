from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    CharField,
    ImageField,
    IntegerField,
    ValidationError,
    ListField,
)
from .models import SendRequest_to_login, Doctor_Profile
from django.contrib.auth.models import User
from .validators import validate_working_schedule
from django.contrib.auth import authenticate, login


class SendRequest_to_login_Serializer(ModelSerializer):
    surname = CharField(write_only=True, required=True)
    phone_number = IntegerField(write_only=True, required=True)
    scanned_document = ImageField(required=True)
    id = IntegerField(read_only=True, required=False)

    class Meta:
        model = SendRequest_to_login
        fields = ("id", "surname", "phone_number", "scanned_document", "email")

    def validate(self, attrs):
        if SendRequest_to_login.objects.filter(
            phone_number=attrs["phone_number"]
        ).exists():
            raise ValidationError(
                {"phone_number": "Sizning surovingiz tekshirish jarayonida"}
            )
        return attrs

    def create(self, validated_data):
        user = SendRequest_to_login.objects.create(**validated_data)
        user.save()
        return user


class DoctorProfileSerializer(ModelSerializer):
    working_schedule = ListField(
        validators=[
            validate_working_schedule,
        ]
    )
    username = CharField(read_only=True)
    # url = HyperlinkedIdentityField(
    #     view_name="main_app:profile.update_username_password", lookup_field="username", read_only=True
    # )

    class Meta:
        model = Doctor_Profile
        fields = [
            "id",
            "username",
            "phone_number",
            "email",
            "working_schedule",
            "specialization",
            "sub_specializations",
        ]

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class DoctorLoginSerializer(ModelSerializer):
    username = CharField(write_only=True, required=True)
    password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "password"]

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise ValidationError("Invalid login credentials")
        else:
            raise ValidationError('Must include "username" and "password"')
        return user

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
