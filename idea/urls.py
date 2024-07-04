from django.urls import path
from idea import views
from comment import views as comment_views


app_name = 'ideas'

urlpatterns = [
    path('list/', views.IdeasListView.as_view(), name='list'),
    path('idea/<int:pk>', views.IdeasDetailView.as_view(), name='detail'),
    path('create/', views.IdeasCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.IdeasUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.IdeasDeleteView.as_view(), name='delete'),
    path('idea/<int:pk>/comment/add/', comment_views.CommentCreateView.as_view(), name='add_comment'),
    path('idea/<int:pk>/comment/edit/<int:comment_pk>/', comment_views.CommentUpdateView.as_view(), name='edit_comment'),
    path('idea/<int:pk>/comment/delete/<int:comment_pk>/', comment_views.CommentDeleteView.as_view(), name='delete_comment'),
    path('idea/<int:pk>/add_likes/', views.AddLike.as_view(), name='add_likes'),
    path('idea/<int:pk>/add_dislikes/', views.DisLike.as_view(), name='add_dislikes'),
]