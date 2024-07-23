from django.urls import path
from user import views


app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.AuthView.as_view(), name='login'),
    path('logout/', views.ExitView.as_view(), name='logout'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('profile/<int:pk>/', views.UserProfile.as_view(), name='profile'),
    path('profile/<int:pk>/ideas/', views.UserIdeas.as_view(), name='user_ideas'),
    path('profile/<int:pk>/following/', views.FollowUser.as_view(), name='following'),
    path('profile/<int:pk>/followers/', views.Followers.as_view(), name='followers'),
    path('profile/<int:pk>/partnerships/', views.UserCoAuthorIdeas.as_view(), name='partnerships'),
    path('profile/<int:pk>/favourites/', views.UserFavouritesIdeas.as_view(), name='favourites'),
    path('profile/<int:pk>/investments/', views.UserInvestmentIdeas.as_view(), name='investments'),
]
