from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Modelo de Usuario Personalizado """
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True) # Opcional
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
