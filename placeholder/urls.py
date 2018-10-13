from django.conf.urls import include, url
from django.contrib import admin
import os
from placeholder_app.urls import placeholder_api_patterns
from placeholder_app.views import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'placeholder_app'),
)

handler403 = 'placeholder.templates.permission_denied_view'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^placeholder/', include('placeholder_app.urls')),
    url(r'^api/', include(placeholder_api_patterns)),
]
