from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import SendRequest_to_login_Serializer, DoctorLoginSerializer
from .models import SendRequest_to_login
from django.contrib.auth import authenticate


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


class Profile_login(ModelViewSet):
    serializer_class = DoctorLoginSerializer
    http_method_names = ["post"]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            response = Response(status=status.HTTP_302_FOUND)
            response["Location"] = "/other-page/"
            return response
        else:
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )


def image_view(request, pk):
    """
    Returns the image with the given PK.
    """
    image = SendRequest_to_login.objects.get(pk=pk)

    response = Response()
    # response.render('image/png')
    response.content = image.image.read()

    return response
