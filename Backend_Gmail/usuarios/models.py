from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="O número de telefone deve estar no formato: '+999999999'. Até 15 dígitos permitidos."
)

class User(models.Model):
    name = models.CharField(max_length=125)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    
    def __str__(self):
        return self.name