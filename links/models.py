import uuid

from django.db import models
from model_utils.models import TimeStampedModel

from link_zipper.settings import SITE


class Link(TimeStampedModel):
    session = models.CharField('Сессия', max_length=32)
    url = models.CharField('Ссылка', max_length=1024)
    zipped_url = models.CharField("Сжатая ссылка", max_length=128)
    clicks = models.IntegerField("Количество кликов", default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.zipped_url = uuid.uuid4()
        super(Link, self).save(*args, **kwargs)

    def increment_clicks(self):
        self.clicks += 1
        self.save()

    @property
    def full_zipped_url(self):
        return f"{SITE}/{self.zipped_url}"
