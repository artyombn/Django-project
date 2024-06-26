from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=15, blank=True)
    last_name = models.CharField(max_length=15, blank=True)
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='user_avatars/', default='user_avatars/no_avatar.png')

    # date_joined =
    # is_active =

    def __str__(self):
        return (f"{self.username}")

    def check_in_group(self, group_name):
        return self.groups.filter(name=group_name).exists()