from django.contrib import admin
from .models import Doctor_user_Registration, SendRequest_to_login

# Register your models here.
admin.site.register(Doctor_user_Registration)
admin.site.register(SendRequest_to_login)
