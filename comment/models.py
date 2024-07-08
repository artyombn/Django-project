from django.db import models
from django.db.models.signals import post_save, post_delete

class Comment(models.Model):
    idea = models.ForeignKey('idea.Idea', related_name='comments', on_delete=models.CASCADE, default=1)
    author = models.ForeignKey('user.User', related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def comment_post(sender, instance, *args, **kwargs):
        from idea.models import Idea
        from notifications.models import Notification
        comment = instance
        sender = comment.author
        idea = Idea.objects.get(id=comment.idea.id)
        user = idea.author
        comment_text = comment.text
        notify = Notification.objects.create(idea=idea, sender=sender, user=user, text_preview=comment_text, notification_type=3)
        notify.save()

    def comment_delete(sender, instance, *args, **kwargs):
        from idea.models import Idea
        from notifications.models import Notification
        comment = instance
        sender = comment.author
        idea = Idea.objects.get(id=comment.idea.id)
        user = idea.author

        notify = Notification.objects.filter(sender=sender, user=user, idea=idea, notification_type=3)
        notify.delete()


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



post_save.connect(Comment.comment_post, sender=Comment)
post_delete.connect(Comment.comment_delete, sender=Comment)
