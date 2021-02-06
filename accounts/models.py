from django.contrib.auth.models import AbstractUser
from django.db import models 
class AppUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
