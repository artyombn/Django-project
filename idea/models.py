from django.db import models
from django.db.models.signals import post_save, post_delete

from notifications.models import Notification
from user.models import Follow



class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='idea_images/', default='idea_images/no_idea.jpg')
    status = models.ForeignKey("IdeaStatus", on_delete=models.CASCADE, default=1)
    co_author = models.ManyToManyField('user.User', through='partnership.CoAuthor', related_name='coauthored_ideas', blank=True)
    investors = models.ManyToManyField('user.User', through='investment.Investor', related_name='investors_ideas', blank=True)


# class IdeaImages(models.Model):
#     idea = models.ForeignKey(Idea, related_name='images', on_delete=models.CASCADE)
#     image2 = models.ImageField(upload_to='idea_images/', default='idea_images/no_idea.jpg')

    def __str__(self):
        return (f"{self.title}/{self.category}/{self.author}")

    def comments_count(self):
        return self.comments.count()

    def idea_follow(sender, instance, created, **kwargs):
        if created:
            idea = instance
            followers = idea.author.follower.all()
            for follow in followers:
                # print(f"Follower: {follow.following.username}")
                notify = Notification(idea=idea, sender=idea.author, user=follow.following, notification_type=9)
                notify.save()
    def idea_follow_delete(sender, instance, **kwargs):
            idea = instance
            followers = idea.author.follower.all()
            for follow in followers:
                notifications = Notification.objects.filter(idea=idea, sender=idea.author, user=follow.following, notification_type=9)
                notifications.delete()



class Likes(models.Model):

    idea = models.ForeignKey(Idea, verbose_name='Idea', on_delete=models.CASCADE)
    author = models.ForeignKey('user.User', verbose_name='User', on_delete=models.CASCADE)

    def user_liked_idea(sender, instance, *args, **kwargs):
        like = instance
        idea = like.idea
        sender = like.author
        notify = Notification(idea=idea, sender=sender, user=idea.author, notification_type=1)
        notify.save()

    def user_unlike_idea(sender, instance, *args, **kwargs):
        like = instance
        idea = like.idea
        sender = like.author

        notify = Notification.objects.filter(idea=idea, sender=sender, notification_type=1)
        notify.delete()



class DisLikes(models.Model):

    idea = models.ForeignKey(Idea, verbose_name='Idea', on_delete=models.CASCADE)
    author = models.ForeignKey('user.User', verbose_name='User', on_delete=models.CASCADE)

    def user_disliked_idea(sender, instance, *args, **kwargs):
        dislike = instance
        idea = dislike.idea
        sender = dislike.author
        notify = Notification(idea=idea, sender=sender, user=idea.author, notification_type=2)
        notify.save()

    def user_undislike_idea(sender, instance, *args, **kwargs):
        dislike = instance
        idea = dislike.idea
        sender = dislike.author

        notify = Notification.objects.filter(idea=idea, sender=sender, notification_type=2)
        notify.delete()


class IdeaStatus(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    updated_by = models.ForeignKey('user.User', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status

class Favourite(models.Model):
    idea = models.ForeignKey(Idea, verbose_name='Idea', on_delete=models.CASCADE, related_name='favourite')
    user = models.ForeignKey('user.User', verbose_name='User', on_delete=models.CASCADE, related_name='user')


# Likes
post_save.connect(Likes.user_liked_idea, sender=Likes)
post_delete.connect(Likes.user_unlike_idea, sender=Likes)
# DisLikes
post_save.connect(DisLikes.user_disliked_idea, sender=DisLikes)
post_delete.connect(DisLikes.user_undislike_idea, sender=DisLikes)
# Idea Follow
post_save.connect(Idea.idea_follow, sender=Idea)
post_delete.connect(Idea.idea_follow_delete, sender=Idea)
