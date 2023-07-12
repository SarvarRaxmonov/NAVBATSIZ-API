from rest_framework import routers
from django.urls import path, include, re_path
from .doctor_panel.views import (
    SendRequest_to_login_view,
    Profile_login_view,
    DoctorProfileView,
)
from .admin_panel.views import All_Requests_of_doctors_to_login_Viewset

router = routers.DefaultRouter()
app_name = "main_app"

router.register(r"send_request", SendRequest_to_login_view, basename="send")
router.register(
    r"all_requests", All_Requests_of_doctors_to_login_Viewset, basename="all_requests"
)
router.register("login", Profile_login_view, basename="login")

urlpatterns = [
    path(
        "request/<id>",
        All_Requests_of_doctors_to_login_Viewset.as_view({"get": "retrieve"}),
        name="request-detail",
    ),
    path("login", Profile_login_view.as_view(), name="login"),
    path(
        "profile/<str:username>",
        DoctorProfileView.as_view({"get": "list"}),
        name="profile-detail",
    ),
]

urlpatterns += router.urls
