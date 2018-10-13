from django.apps import AppConfig
import django.utils.timezone as tz
import logging


log = logging.getLogger('dog')

class DogConfig(AppConfig):
    name = 'dog_app'
    verbose_name = 'Dog Application'

    def ready(self):
        pass