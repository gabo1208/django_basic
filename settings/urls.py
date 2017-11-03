"""softwareII URL Configuration"""

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    # Admin urls
    url(r'^admin/', admin.site.urls),
    # Main Views
    url(r'^', include('apps.main.urls')),
    # User Views
    url(r'^user/', include('apps.users.urls', namespace='users')),
    # Api view
    url(r'^api/', include('apps.api.urls', namespace='api')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
