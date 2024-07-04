from django.urls import path
from partnership import views


app_name = 'partnership'

urlpatterns = [
    path('', views.CoAuthorsView.as_view(), name='list'),
]