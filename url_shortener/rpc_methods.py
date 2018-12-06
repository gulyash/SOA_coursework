from modernrpc.core import rpc_method

from url_shortener.models import Url
from url_shortener.tokenizer import Tokenizer


@rpc_method
def urls():
    response = list(Url.objects.all().order_by('-id').values())
    return response


@rpc_method
def get_token(url):
    token = Tokenizer().create_token(url)
    return token
