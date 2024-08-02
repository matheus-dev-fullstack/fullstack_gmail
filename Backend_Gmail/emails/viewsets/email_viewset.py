from rest_framework.viewsets import ModelViewSet

from emails.models import Email
from emails.serializers.email_serializer import EmailSerializer

class EmailViewSet(ModelViewSet):
    serializer_class = EmailSerializer
    
    def get_queryset(self):
        return Email.objects.all().order_by('-date')
