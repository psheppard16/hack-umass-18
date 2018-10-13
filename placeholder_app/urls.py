import os
from django.conf.urls import include, url
from rest_framework import routers
from placeholder_app.api import *
from placeholder_app.views import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'placeholder_app'),
)

router = routers.DefaultRouter(trailing_slash=False)

placeholder_api_patterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = [
    # url(r'^home', HomeView, name="home"),
]