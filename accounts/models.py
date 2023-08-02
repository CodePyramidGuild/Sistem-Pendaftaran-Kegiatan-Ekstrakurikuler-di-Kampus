from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    alamat = models.CharField(max_length=100)
    nomor_telepon = models.CharField(max_length=15)

    def __str__(self):
        return self.username
