from django.urls import path
from comment import views


app_name = 'comment'

urlpatterns = [
    path('', views.comments_list_view, name='comments_index'),
    path('list/', views.CommentListView.as_view(), name='list'),
    path('comment/<int:pk>', views.CommentDetailView.as_view(), name='detail'),
    path('create/', views.CommentCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.CommentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.CommentDeleteView.as_view(), name='delete'),
]
