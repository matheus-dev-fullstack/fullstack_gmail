from rest_framework.viewsets import ModelViewSet

from usuarios.models import User
from usuarios.serializers.user_serializer import UserSerializer

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all().order_by('name')
