from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from contacts.views import contact_view, status_view


urlpatterns = [
    path('ideas/', include('idea.urls', namespace='ideas')),
    path('', include('idea.urls', namespace='ideas')),
    path('categories/', include('category.urls')),
    path('comments/', include('comment.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('users/', include('user.urls', namespace='users')),
    path("contacts/", contact_view),
    path("status/<str:task_id>/", status_view),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)