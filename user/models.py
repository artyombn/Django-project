from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=15, blank=True)
    last_name = models.CharField(max_length=15, blank=True)
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField(unique=True)

    # password =
    # date_joined =
    # is_active =
    # is_superuser =

    def __str__(self):
        return (f"{self.username}")