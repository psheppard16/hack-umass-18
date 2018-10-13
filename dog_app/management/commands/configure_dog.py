from django.core.management.base import BaseCommand, CommandError
from dog_app.models import *

import logging
from django.utils import timezone

log = logging.getLogger('dog')


class Command(BaseCommand):
    help = 'Configures models for the dog application.'

    def handle(self, *args, **options):
        """Adds default entries for the dog app.
            :returns: None
            """

    log.info("Configuration complete")
