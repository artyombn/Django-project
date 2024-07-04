from django.db import models

class CoAuthor(models.Model):

    idea = models.ForeignKey('idea.Idea', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.idea.title} - {self.role}'
