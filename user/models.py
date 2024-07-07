from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete


class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=15, blank=True)
    last_name = models.CharField(max_length=15, blank=True)
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='user_avatars/', default='user_avatars/no_avatar.png')

    # date_joined =
    # is_active =

    def __str__(self):
        return (f"{self.username}")

    def check_in_group(self, group_name):
        return self.groups.filter(name=group_name).exists()

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

    def user_follow(sender, instance, *args, **kwargs):
        from notifications.models import Notification
        follow = instance
        sender = follow.following
        following = follow.follower
        notify = Notification.objects.create(sender=sender, user=following, notification_type=4)
        notify.save()

    def user_unfollow(sender, instance, *args, **kwargs):
        from notifications.models import Notification
        follow = instance
        sender = follow.following
        following = follow.follower

        notify = Notification.objects.filter(sender=sender, user=following, notification_type=4)
        notify.delete()


post_save.connect(Follow.user_follow, sender=Follow)
post_delete.connect(Follow.user_unfollow, sender=Follow)