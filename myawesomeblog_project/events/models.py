from distutils.command.upload import upload
from django.db import models

class Event(models.Model):
    event_image = models.ImageField('фото', upload_to='event_images/')
    event_text = models.CharField('описание', max_length=300)
    upload = models.FileField(upload_to='uploads/%Y%m%d/', blank=True) 