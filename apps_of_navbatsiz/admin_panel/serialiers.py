from rest_framework.serializers import (
    ModelSerializer,
    ImageField,
    HyperlinkedIdentityField,
    ModelField,
)
from apps_of_navbatsiz.doctor_panel.models import SendRequest_to_login


class All_Requests_of_doctors_to_login_update_serializer(ModelSerializer):
    scanned_document = ImageField(required=False)
    # pk = ModelField(model_field=SendRequest_to_login._meta.get_field('pk'), required=False)
    url = HyperlinkedIdentityField(
        view_name="main_app:request-detail", lookup_field="id", read_only=True
    )

    class Meta:
        model = SendRequest_to_login
        fields = [
            "id",
            "surname",
            "phone_number",
            "scanned_document",
            "activate_profile",
            "url",
        ]

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
