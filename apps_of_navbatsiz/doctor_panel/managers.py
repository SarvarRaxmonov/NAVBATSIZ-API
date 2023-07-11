from django.db import models


class Doctor_manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()
