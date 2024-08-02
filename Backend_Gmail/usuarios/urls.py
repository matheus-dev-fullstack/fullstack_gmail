from django.urls import path, include
from rest_framework import routers

from usuarios import viewsets

router = routers.SimpleRouter()
router.register(r"users", viewsets.UserViewSet, basename="users")

urlpatterns = [
    path("", include(router.urls)),
]
