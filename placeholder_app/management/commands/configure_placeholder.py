from django.core.management.base import BaseCommand, CommandError
from placeholder_app.models import *

import logging
from django.utils import timezone

log = logging.getLogger('placeholder')


class Command(BaseCommand):
    help = 'Configures models for the placeholder application.'

    def handle(self, *args, **options):
        """Adds default entries for the placeholder app.
            :returns: None
            """

    log.info("Configuration complete")
