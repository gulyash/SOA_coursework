from rest_framework import serializers

from url_shortener.models import Url


class UrlSerializer(serializers.Serializer):
    class Meta:
        model = Url
        fields = ('__all__',)
