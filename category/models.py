import os

from django.db import models

from Brainwave import settings


class Category(models.Model):
    title = models.CharField(unique=True, max_length=32)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='idea_images/', default='idea_images/non_category.jpg')

    def __str__(self):
        return (f"{self.title}")
