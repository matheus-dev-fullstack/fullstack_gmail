from django.urls import path, include
from rest_framework import routers

from emails import viewsets

router = routers.SimpleRouter()
router.register(r"emails", viewsets.EmailViewSet, basename="emails")

urlpatterns = [
    path("", include(router.urls)),
]
