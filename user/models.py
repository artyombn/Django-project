from django.db import models
from django.db.models import EmailField


class User(models.Model):
    username = models.CharField(max_length=15)
    first_name = models.CharField(max_length=15, blank=True)
    last_name = models.CharField(max_length=15, blank=True)
    email = EmailField()

    # password =
    # date_joined =
    # is_active =
    # is_superuser =

    def __str__(self):
        return (f"Username: {self.username} -- \n"
                f"Email: {self.email}")
