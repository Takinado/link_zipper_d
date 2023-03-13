from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from links.models import Link
from links.serializers import LinkSerializer, RedirectSerializer


class LinkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Link.objects.all().order_by("-created")
    serializer_class = LinkSerializer
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'api.html'

    def perform_create(self, serializer):
        if not self.request.session.session_key:
            self.request.session.save()
        session_id = self.request.session.session_key
        serializer.save(session=session_id)

    def get_queryset(self):
        """
        Переопределение queryset для действия list.
        """
        queryset = self.queryset
        if self.action == "list":
            session_key = self.request.session.session_key
            queryset = queryset.filter(session=session_key)

        return queryset


class RedirectViewSet(viewsets.GenericViewSet):
    serializer_class = RedirectSerializer
    queryset = Link.objects.all().filter()
    lookup_field = "zipped_url"

    def retrieve(self, request, zipped_url=None):
        """
        Редирект по ссылке
        """
        instance = self.get_object()
        instance.increment_clicks()
        cached_url = cache.get(zipped_url)

        if cached_url:
            print("from cache")
            return HttpResponseRedirect(cached_url)
        else:
            print("from db")
            cache.set(zipped_url, instance.url, settings.REDIS_AGE)
            serializer = self.get_serializer(instance)
            return HttpResponseRedirect(serializer.data["url"])
