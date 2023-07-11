from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    SendRequest_to_login_Serializer,
    DoctorLoginSerializer,
    DoctorProfileSerializer,
)
from .models import SendRequest_to_login, Doctor_Profile
from django.contrib.auth import authenticate, login
from rest_framework import status
from django.contrib.auth.models import User


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


class DoctorProfileView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Doctor_Profile.objects.all()
    serializer_class = DoctorProfileSerializer

    def get(self, request, username=None):
        user = User.objects.get(username=username)
        if user is not None:
            instance = Doctor_Profile.objects.filter(username=user.id).values()
            validate_data = DoctorProfileSerializer(instance, many=True)
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

    def put(self, request, username=None):
        user = User.objects.get(username=username)
        profile = Doctor_Profile.objects.get(username=user.id)
        if profile is not None:
            serializer = self.serializer_class(data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=201)
        else:
            return Response(
                {"status": status.HTTP_401_UNAUTHORIZED, "message": "Wrong username"}
            )


class Profile_login_view(APIView):
    serializer_class = DoctorLoginSerializer
    http_method_names = ["post"]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            response = Response(status=status.HTTP_302_FOUND)
            response["Location"] = f"profile/{username}"
            return response
        else:
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

    def get_extra_actions():
        return []


def image_view(request, pk):
    """
    Returns the image with the given PK.
    """
    image = SendRequest_to_login.objects.get(pk=pk)

    response = Response()
    # response.render('image/png')
    response.content = image.image.read()

    return response
