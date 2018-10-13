from django.core.management.base import BaseCommand, CommandError
from argue_app.models import *

import logging
from django.utils import timezone

log = logging.getLogger('argue')


class Command(BaseCommand):
    help = 'Configures models for the argue application.'

    def handle(self, *args, **options):
        """Adds default entries for the argue app.
            :returns: None
            """

    log.info("Configuration complete")
