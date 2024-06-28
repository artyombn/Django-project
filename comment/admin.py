from django.contrib import admin
from .models import Comment, CommentLikes


admin.site.register(Comment)
admin.site.register(CommentLikes)