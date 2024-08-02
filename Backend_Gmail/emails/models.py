from django.db import models

# Create your models here.
class Email(models.Model):
    author_name = models.CharField(max_length=125)
    author_email = models.EmailField(max_length=100)
    title = models.CharField(max_length=125)
    category = models.CharField(max_length=125)
    message = models.CharField(max_length=255)
    date = models.DateTimeField()
