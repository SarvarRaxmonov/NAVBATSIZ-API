from rest_framework import serializers
from .models import SendRequest_to_login
from django.contrib.auth.models import User


class SendRequest_to_login_Serializer(serializers.ModelSerializer):
    surname = serializers.CharField(write_only=True, required=True)
    phone_number = serializers.IntegerField(write_only=True, required=True)
    scanned_document = serializers.ImageField(required=True)
    id = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = SendRequest_to_login
        fields = ("id", "surname", "phone_number", "scanned_document", "email")

    def validate(self, attrs):
        if SendRequest_to_login.objects.filter(
            phone_number=attrs["phone_number"]
        ).exists():
            raise serializers.ValidationError(
                {"phone_number": "Sizning surovingiz tekshirish jarayonida"}
            )
        return attrs

    def create(self, validated_data):
        user = SendRequest_to_login.objects.create(**validated_data)
        user.save()
        return user


class DoctorLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
