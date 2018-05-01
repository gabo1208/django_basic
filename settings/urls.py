"""softwareII URL Configuration"""

from django.urls import re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

app_name = 'urls'
urlpatterns = [
    # Admin Urls
    re_path('^admin/', admin.site.urls),
    # User Urls
    re_path('^user/', include('apps.users.urls', namespace='users')),
    # Chat Urls
    #re_path('^chat/', include('apps.chat.urls', namespace='chat')),
    # Quiniela Urls
    re_path('^user/quinielas/', include('apps.quiniela.urls', namespace='quiniela')),
    # Api Urls
    #re_path('^api/', include('apps.api.urls', namespace='api')),
    # Oauth2 Urls
    #re_path('^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # Main Urls
    re_path('^', include('apps.main.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
