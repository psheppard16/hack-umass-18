from django.apps import AppConfig
import django.utils.timezone as tz
import logging


log = logging.getLogger('placeholder')

class PlaceholderConfig(AppConfig):
    name = 'placeholder_app'
    verbose_name = 'Placeholder Application'

    def ready(self):
        pass