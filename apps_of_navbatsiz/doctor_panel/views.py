from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .serializers import (
    SendRequest_to_login_Serializer,
    DoctorLoginSerializer,
    DoctorProfileSerializer,
)
from .models import SendRequest_to_login, Doctor_Profile
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import action


class SendRequest_to_login_view(ModelViewSet):
    serializer_class = SendRequest_to_login_Serializer
    http_method_names = ["post"]
    queryset = SendRequest_to_login.objects.all()
    throttle_scope = "for_anon_user"

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)


class Profile_login_view(APIView):
    serializer_class = DoctorLoginSerializer
    http_method_names = ["post"]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        validate = self.serializer_class(
            data={"username": username, "password": password}
        )
        if validate.is_valid(raise_exception=True):
            token, created = Token.objects.get_or_create(user=validate.validated_data)
            response = Response({"token": token.key})
            return response
        else:
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

    def get_extra_actions():
        return []


class DoctorProfileView(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    serializer_class = DoctorProfileSerializer
    queryset = Doctor_Profile.objects.all()

    def get(self, request, username=None):
        user = User.objects.get(username=username)
        if user is not None:
            instance = Doctor_Profile.objects.filter(username=user.id).values()
            validate_data = DoctorProfileSerializer(
                instance, context={"request": request}, many=True
            )
            return Response(
                {"status": status.HTTP_200_OK, "user profile data": validate_data.data}
            )
        else:
            return Response(
                {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "You are not authorized to view this page",
                }
            )

    def get_object(self, username=None):
        try:
            user = User.objects.get(username=username)
            return Doctor_Profile.objects.get(username=user.id)
        except Doctor_Profile.DoesNotExist:
            return Response(
                {"status": status.HTTP_401_UNAUTHORIZED, "message": "Wrong username"}
            )

    def patch(self, request, username=None):
        instance = self.get_object(username)
        if instance:
            serializer = self.serializer_class(
                instance, data=request.data, partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=201)

    @action(detail=True, methods=["put"])
    def update_username_password(self, request, username=None):
        instance = User.objects.get(username=username)
        if instance:
            serializer = DoctorLoginSerializer(
                instance, data=request.data, partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=201)
        else:
            return Response(
                {"status": status.HTTP_401_UNAUTHORIZED, "message": "Wrong username"}
            )
