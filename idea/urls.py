from django.urls import path
from idea import views


app_name = 'ideas'

urlpatterns = [
    path('', views.ideas_list_view, name='ideas_index'),
    path('list/', views.IdeasListView.as_view(), name='list'),
    path('idea/<int:pk>', views.IdeasDetailView.as_view(), name='detail'),
    path('create/', views.IdeasCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.IdeasUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.IdeasDeleteView.as_view(), name='delete'),
]
