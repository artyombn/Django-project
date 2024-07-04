from django.db import models

class Comment(models.Model):
    idea = models.ForeignKey('idea.Idea', related_name='comments', on_delete=models.CASCADE, default=1)
    author = models.ForeignKey('user.User', related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"Text: {self.text}, -- "
            f"Under idea: {self.idea}, -- "
            f"Author: {self.author}, -- "
            f"Created_at: {self.created_at}"
        )

class CommentLikes(models.Model):

    author = models.ForeignKey('user.User', verbose_name='User', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, verbose_name='Comment', on_delete=models.CASCADE)
