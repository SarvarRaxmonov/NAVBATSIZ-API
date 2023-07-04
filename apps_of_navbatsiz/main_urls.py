from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
app_name = 'main_app'

urlpatterns = [
    path('', include(router.urls)),
]

# router.register('ariza',view,basename='')



urlpatterns = router.urls


