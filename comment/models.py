from django.db import models
from idea.models import Idea
from user.models import User

class Comment(models.Model):
    idea = models.ForeignKey(Idea, related_name='comments', on_delete=models.CASCADE, default=1)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"Text: {self.text}, -- "
            f"Under idea: {self.idea}, -- "
            f"Author: {self.author}, -- "
            f"Created_at: {self.created_at}"
        )
