from django.db import models
from user.models import User

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        (1, 'LikeIdea'),
        (2, 'DisLikeIdea'),
        (3, 'Comment'),
        (4, 'Follow'),
        (5, 'CoAuthorRequest'),
        (6, 'CoAuthorApproved'),
        (7, 'CoAuthorRejected'),
        (8, 'CoAuthorStopped'),
        (9, 'IdeaFollowed'),
        (10, 'Investor'),
    )

    idea = models.ForeignKey('idea.Idea', on_delete=models.CASCADE, related_name='noti_idea', blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='noti_from_user')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='noti_to_user')
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
    text_preview = models.CharField(max_length=90, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)