from django.http import HttpResponseRedirect

from rest_framework import viewsets, status
from rest_framework.response import Response

from links.models import Link
from links.serializers import LinkSerializer, RedirectSerializer


class LinkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Link.objects.all().order_by('-created')
    serializer_class = LinkSerializer

    def perform_create(self, serializer):
        serializer.save(session=self.request.session.session_key)

    def list(self, request, *args, **kwargs):
        session_key = request.session.session_key
        queryset = self.filter_queryset(self.get_queryset()).filter(session=session_key)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        response = Response(serializer.data)

        return response


class RedirectViewSet(viewsets.GenericViewSet):

    serializer_class = RedirectSerializer
    queryset = Link.objects.all().filter()
    lookup_field = 'zipped_url'

    def retrieve(self, request, zipped_url=None):
        """
        Редирект по ссылке
        """
        instance = self.get_object()
        instance.increment_clicks()
        serializer = self.get_serializer(instance)
        return HttpResponseRedirect(serializer.data['url'])
