from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import SendRequest_to_login_Serializer
from .models import SendRequest_to_login


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


def image_view(request, pk):
    """
    Returns the image with the given PK.
    """
    image = SendRequest_to_login.objects.get(pk=pk)

    response = Response()
    # response.render('image/png')
    response.content = image.image.read()

    return response
