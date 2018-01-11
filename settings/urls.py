"""softwareII URL Configuration"""

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

app_name = 'settings'
urlpatterns = [
    # Admin Urls
    path('admin/', admin.site.urls),
    # User Views
    path('user/', include('apps.users.urls', namespace='users')),
    # Api Urls
    path('api/', include('apps.api.urls', namespace='api')),
    # Oauth2 Urls
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # Main Views
    path('', include('apps.main.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
