from django.db.models.signals import post_delete
from django.dispatch import receiver

from partnership.models import PreCoAuthor
from notifications.models import Notification

@receiver(post_delete, sender=PreCoAuthor)
def precoauthor_reject_signal(sender, instance, **kwargs):
    if instance.is_rejected:
        idea = instance.idea
        user = instance.user
        notify = Notification(
            idea=idea,
            sender=user,
            user=user,
            notification_type=7
        )
        notify.save()