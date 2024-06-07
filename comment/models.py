from django.db import models
from idea.models import Idea
from user.models import User

class Comment(models.Model):
    idea = models.ForeignKey(Idea, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"Comment under idea ({self.idea}),"
                f"author ({self.author}),"
                f"text ({self.text}),"
                f"created_at ({self.created_at})")
