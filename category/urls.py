from django.urls import path, include
from category import views



app_name = 'category'

urlpatterns = [
    path('', views.category_list_view, name='categories_index'),
    path('list/', views.CategoryListView.as_view(), name='list'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='detail'),
    path('create/', views.CategoryCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.CategoryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.CategoryDeleteView.as_view(), name='delete'),
]