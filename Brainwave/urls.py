from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from contacts.views import contact_view, status_view


urlpatterns = [
    path('ideas/', include('idea.urls', namespace='ideas')),
    path('', include('idea.urls', namespace='ideas')),
    path('categories/', include('category.urls')),
    path('comments/', include('comment.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('users/', include('user.urls')),
    path("contacts/", contact_view),
    path("status/<str:task_id>/", status_view),
]
