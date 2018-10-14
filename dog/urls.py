from django.conf.urls import include, url
from django.contrib import admin
import os
from dog_app.urls import dog_api_patterns
from dog_app.views import *
from django.conf import settings
from django.conf.urls.static import static


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'dog_app'),
)

handler403 = 'dog.templates.permission_denied_view'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dog/', include('dog_app.urls')),
    url(r'^api/', include(dog_api_patterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)