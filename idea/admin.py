from django.contrib import admin
from idea.models import Idea, Likes, DisLikes, IdeaStatus

# Register your models here.
admin.site.register(Idea)
admin.site.register(Likes)
admin.site.register(DisLikes)
admin.site.register(IdeaStatus)