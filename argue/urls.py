from django.conf.urls import include, url
from django.contrib import admin
import os
from argue_app.urls import argue_api_patterns
from argue_app.views import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'argue_app'),
)

handler403 = 'argue.templates.permission_denied_view'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^argue/', include('argue_app.urls')),
    url(r'^api/', include(argue_api_patterns)),
]
