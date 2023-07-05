from django.apps import AppConfig


class DoctorPanelConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps_of_navbatsiz.doctor_panel"
    label = "doctor_panel"

    def ready(self):
        from apps_of_navbatsiz.doctor_panel import signals
