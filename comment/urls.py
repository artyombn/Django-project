from django.urls import path
from comment.views import comments_list_view


app_name = 'comment'

urlpatterns = [
    path('', comments_list_view, name='comments_index'),
]
