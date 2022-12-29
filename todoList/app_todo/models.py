from django.db import models

# Create your models here.
class AppUser(models.Model):
    full_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=200)
    