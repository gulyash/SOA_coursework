from django.utils.crypto import get_random_string

from url_shortener.models import Url


class Tokenizer:
    SHORT_URL_LEN = 8

    def create_token(self, url):
        token = self.get_unique_token()
        url, created = Url.objects.get_or_create(url=url)
        if created:
            url.token = token
            url.full_clean()
            url.save()
        return url.token

    def get_unique_token(self):
        tokens = set(Url.objects.all().values_list('token', flat=True))
        while True:
            token = get_random_string(length=self.SHORT_URL_LEN)
            if token not in tokens:
                return token
