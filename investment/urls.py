from django.urls import path, include
from investment import views

app_name = 'investment'

urlpatterns = [
    path('', views.InvestorsView.as_view(), name='list')
]