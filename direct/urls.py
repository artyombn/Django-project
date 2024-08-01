from django.urls import path

from . import views

app_name = 'direct'

urlpatterns = [
    path('messages/', views.MessagesList.as_view(), name='messages'),
]