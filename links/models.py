import uuid

from django.conf import settings
from django.contrib.sessions.models import Session
from django.core.cache import cache
from django.db import models
from django.db.models.signals import pre_delete
from model_utils.models import TimeStampedModel


class Link(TimeStampedModel):
    session = models.CharField("Сессия", max_length=32)
    url = models.CharField("Ссылка", max_length=1024)
    zipped_url = models.CharField("Сжатая ссылка", max_length=1024)
    clicks = models.IntegerField("Количество кликов", default=0)

    def save(self, *args, **kwargs):
        if not self.pk and not self.zipped_url:
            self.zipped_url = uuid.uuid4()
        super(Link, self).save(*args, **kwargs)

    def increment_clicks(self):
        self.clicks += 1
        self.save()

    @property
    def full_zipped_url(self):
        return f"{settings.SITE}/{self.zipped_url}"


def sessionend_handler(sender, **kwargs):
    session_key = kwargs.get("instance").session_key
    queryset = Link.objects.filter(session=session_key)
    cache.delete_many(list(queryset.values_list("zipped_url", flat=True)))
    queryset.delete()


pre_delete.connect(sessionend_handler, sender=Session)
