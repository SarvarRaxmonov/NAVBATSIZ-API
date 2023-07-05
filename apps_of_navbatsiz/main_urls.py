from rest_framework import routers
from django.urls import path, include, re_path
from .doctor_panel.views import SendRequest_to_login_view
from .admin_panel.views import All_Requests_of_doctors_to_login_Viewset

router = routers.DefaultRouter()
app_name = "main_app"

router.register(r"send_request", SendRequest_to_login_view, basename="send")
router.register(
    r"all_requests", All_Requests_of_doctors_to_login_Viewset, basename="all_requests"
)
urlpatterns = [
    # re_path(r"(?P<endpoint>.+)/", include(router.urls)),
    path(
        "request/<id>",
        All_Requests_of_doctors_to_login_Viewset.as_view({"get": "retrieve"}),
        name="request-detail",
    ),
]

urlpatterns += router.urls
