import os
from django.conf.urls import include, url
from rest_framework import routers
from dog_app.api import *
from dog_app.views import *
from . import views


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'dog_app'),
)

router = routers.DefaultRouter(trailing_slash=False)

dog_api_patterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = [
    url(r'^home/', HomeView, name="home"),
    url(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
]

