from django.urls import path
from notifications import views

app_name = 'notifications'

urlpatterns = [
    path('', views.ShowNotifications, name='show-notifications'),
    path('delete/<int:id>', views.DeleteNotification, name='delete-notification'),
    path('deleteall/', views.DeleteAllNotifications, name='delete-all-notifications'),
]
