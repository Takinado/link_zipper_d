from rest_framework import serializers

from links.models import Link


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    full_zipped_url = serializers.SerializerMethodField()
    session = serializers.CharField(read_only=True, max_length=32)
    url = serializers.CharField(max_length=1024)
    clicks = serializers.IntegerField(read_only=True, default=0)

    class Meta:
        model = Link
        fields = ['session', 'url', 'full_zipped_url', 'clicks']

    def get_full_zipped_url(self, obj):
        return obj.full_zipped_url


class RedirectSerializer(serializers.ModelSerializer):
    url = serializers.CharField(max_length=1024)
    zipped_url = serializers.CharField(read_only=True, max_length=128)

    class Meta:
        model = Link
        fields = ['url', 'zipped_url']

