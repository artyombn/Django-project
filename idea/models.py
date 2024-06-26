from django.db import models
from category.models import Category
from user.models import User


# STATUS_CHOICES = [
#     ('active', 'Active'),
#     ('pending', 'Pending'),
#     ('completed', 'Completed'),
# ]


class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='idea_images/', default='idea_images/no_idea.jpg')


# class IdeaImages(models.Model):
#     idea = models.ForeignKey(Idea, related_name='images', on_delete=models.CASCADE)
#     image2 = models.ImageField(upload_to='idea_images/', default='idea_images/no_idea.jpg')

    def __str__(self):
        return (f"{self.title}/{self.category}/{self.author}")

    def comments_count(self):
        return self.comments.count()