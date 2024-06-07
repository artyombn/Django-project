from django.db import models

class Category(models.Model):
    title = models.CharField(unique=True, max_length=32)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"Category ({self.title}),"
                f"description ({self.description}),"
                f"created_at ({self.created_at})")

