from django.contrib import admin
from idea.models import Idea, Likes, DisLikes, IdeaStatus, Favourite

# Register your models here.
admin.site.register(Idea)
admin.site.register(Likes)
admin.site.register(DisLikes)
admin.site.register(IdeaStatus)
admin.site.register(Favourite)