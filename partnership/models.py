from django.db import models
from django.db.models.signals import post_save, post_delete

from notifications.models import Notification

class CoAuthor(models.Model):

    idea = models.ForeignKey('idea.Idea', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.idea.title} - {self.role}'

    def coauthor_approve_signal(sender, instance, *args, **kwargs):
        coauthor = instance
        idea = coauthor.idea
        user = coauthor.user
        # role = coauthor.role
        notify = Notification(idea=idea, sender=user, user=user, notification_type=6)
        notify.save()

    def coauthor_stop_signal(sender, instance, *args, **kwargs):
        coauthor = instance
        idea = coauthor.idea
        user = coauthor.user
        notify = Notification.objects.filter(idea=idea, sender=user, user=user, notification_type=6)
        notify2 = Notification(idea=idea, sender=user, user=idea.author, notification_type=8)
        notify.delete()
        notify2.save()


class PreCoAuthor(models.Model):
    idea = models.ForeignKey('idea.Idea', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    is_rejected = models.BooleanField(default=False)

    def preco_author_request(sender, instance, *args, **kwargs):
        precoauthor = instance
        sender = precoauthor.user
        idea = precoauthor.idea
        notify_recipient = Notification(idea=idea, sender=sender, user=idea.author, notification_type=5)
        notify_sender = Notification(idea=idea, sender=sender, user=sender, notification_type=5)
        notify_recipient.save()
        notify_sender.save()

    def preco_author_delete_request(sender, instance, *args, **kwargs):
        precoauthor = instance
        sender = precoauthor.user
        idea = precoauthor.idea
        notify = Notification.objects.filter(idea=idea, sender=sender, notification_type=5)
        notify.delete()


# Pre-Co-Authors
post_save.connect(PreCoAuthor.preco_author_request, sender=PreCoAuthor)
post_delete.connect(PreCoAuthor.preco_author_delete_request, sender=PreCoAuthor)
# Co-Authors
post_save.connect(CoAuthor.coauthor_approve_signal, sender=CoAuthor)
post_delete.connect(CoAuthor.coauthor_stop_signal, sender=CoAuthor)