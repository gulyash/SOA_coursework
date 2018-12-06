from django.core.exceptions import ValidationError
from django.forms import URLField
from django.utils.crypto import get_random_string

from url_shortener.models import Url


class InvalidUrlException(Exception):
    pass


class Tokenizer:
    SHORT_URL_LEN = 8

    def create_token(self, long_url):
        url = None
        token = self.get_unique_token()
        try:
            url, created = Url.objects.get_or_create(url=long_url)
            if created:
                url.token = token
                url.full_clean()
                url.save()
            return url.token
        except ValidationError as e:
            if url:
                url.delete()
            raise InvalidUrlException(f"{long_url} is not a valid URL.")

    def get_unique_token(self):
        tokens = set(Url.objects.all().values_list('token', flat=True))
        while True:
            token = get_random_string(length=self.SHORT_URL_LEN)
            if token not in tokens:
                return token


def is_valid_url(url):
    url_form_field = URLField()
    try:
        url = url_form_field.clean(url)
    except ValidationError as e:
        return False
    return True
