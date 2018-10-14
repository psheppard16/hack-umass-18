from django.db import models
import django.utils.timezone as tz
from django.db.models.signals import post_save
from django.dispatch import receiver
from dog.settings import BASE_DIR
from django.core.files.base import ContentFile
import dog_app.label_detection as ld
from PIL import Image
import os.path
from django.core.files import File  # you need this somewhere
import urllib
import os

class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

# method for updating
@receiver(post_save, sender=Photo, dispatch_uid="process_iamge")
def process_photo(sender, instance, **kwargs):
    # 2, open it from the location django stuck it
    thumb = Image.open(instance.file.path)
    thumb.thumbnail((100, 100))

    # make tmp filename based on id of the model
    filename = str(instance.id)

    # 3. save the thumbnail to a temp dir

    temp_image = open(os.path.join(BASE_DIR, filename), 'w')
    thumb.save(temp_image, 'JPEG')

    ld.run_doggo_detection(filename)