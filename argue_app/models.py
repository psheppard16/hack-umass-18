from django.db import models
import django.utils.timezone as tz

# class Data(models.Model):
#     date_time = models.DateTimeField(blank=False)
#     type = models.ForeignKey('DataType', blank=False, on_delete=True)
#     value = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)