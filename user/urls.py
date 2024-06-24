from django.urls import path
from user import views


app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.AuthView.as_view(), name='login'),
    path('logout/', views.ExitView.as_view(), name='logout'),
    path('', views.users_list_view, name='users_list'),
    path('profile/<int:pk>/', views.UserProfile.as_view(), name='profile'),
]
