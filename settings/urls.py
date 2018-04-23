"""softwareII URL Configuration"""

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

app_name = 'urls'
urlpatterns = [
    # Admin Urls
    path('admin/', admin.site.urls),
    # User Urls
    path('user/', include('apps.users.urls', namespace='users')),
    # Chat Urls
    path('chat/', include('apps.chat.urls', namespace='chat')),
    # Quiniela Urls
    path('quiniela/', include('apps.quiniela.urls', namespace='quiniela')),
    # Api Urls
    path('api/', include('apps.api.urls', namespace='api')),
    # Oauth2 Urls
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # Main Urls
    path('', include('apps.main.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
