from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from idea import views

from contacts.views import contact_view, status_view, about_view


urlpatterns = [
    path('ideas/', include('idea.urls', namespace='ideas')),
    path('', views.index, name='index'),
    path('categories/', include('category.urls', namespace='categories')),
    path('comments/', include('comment.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    path('users/', include('user.urls', namespace='users')),
    path("contacts/", contact_view, name='contact_us'),
    path("about/", about_view, name='about'),
    path("status/<str:task_id>/", status_view),
    path('partnership/', include('partnership.urls', namespace='partnership')),
    path('investments/', include('investment.urls', namespace='investments')),
    path('notifications/', include('notifications.urls', namespace='notifications'))
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)