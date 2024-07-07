from django.urls import path
from user import views


app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.AuthView.as_view(), name='login'),
    path('logout/', views.ExitView.as_view(), name='logout'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('profile/<int:pk>/', views.UserProfile.as_view(), name='profile'),
    path('profile/<int:pk>/following/', views.FollowUser.as_view(), name='following'),
]
