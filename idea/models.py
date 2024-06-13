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

    # updated_at = models.DateTimeField(auto_now=True)
    # comment = models.ManyToManyField(Comment)
    # rating = models.IntegerField(default=0)
    # partners = models.ManyToManyField(User)
    # investors = models.ManyToManyField(Investment)
    # status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    # image = models.ImageField(upload_to='idea_images/', null=True, blank=True)




    def __str__(self):
        return (f"{self.title}")