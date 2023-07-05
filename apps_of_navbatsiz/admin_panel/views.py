from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .serialiers import All_Requests_of_doctors_to_login_update_serializer
from apps_of_navbatsiz.doctor_panel.models import SendRequest_to_login



class All_Requests_of_doctors_to_login_Viewset(ModelViewSet):
    serializer_class = All_Requests_of_doctors_to_login_update_serializer
    http_method_names = ["get", "put"]
    Authentication = [IsAdminUser]
    ordering = ("phone_number",)

    def put(self, request, id=None, *args, **kwargs):
        instance = SendRequest_to_login.objects.get(pk=id)
        serializer = All_Requests_of_doctors_to_login_update_serializer(
            instance, data=request.data, context={"request": request}, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"data": serializer.data})
        return Response({"error": serializer.error_messages})

    def get_queryset(self):
        return SendRequest_to_login.objects.all()

    def get(self, request):
        serializer = self.serializer_class(
            self.get_queryset(), context={"request": request}
        )
        return Response({"data": serializer.data})

    def retrieve(self, request, id=None):
        try:
            single_data = self.get_serializer(SendRequest_to_login.objects.get(pk=id))
            return Response(single_data.data)
        except SendRequest_to_login.DoesNotExist:
            return Response({"message": "uzur bunday request kelib tushmagan"})
