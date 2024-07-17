from django.urls import path
from partnership import views


app_name = 'partnership'

urlpatterns = [
    path('', views.CoAuthorsView.as_view(), name='list'),
    path('create/<int:pk>', views.PreCoAuthorView.as_view(), name='pre_coauthor_create'),
    path('approve/<int:notification_id>', views.ApproveCoAuthor.as_view(), name='approve_coauthor'),
    path('reject/<int:notification_id>', views.RejectCoAuthor.as_view(), name='reject_coauthor'),
    path('delete/<int:pk>', views.PreCoAuthorDeleteView.as_view(), name='pre_coauthor_delete'),
    path('stop_being_coauthor/<int:pk>', views.StopBeingCoAuthor.as_view(), name='stop_being_coauthor'),
]