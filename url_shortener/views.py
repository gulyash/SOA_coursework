import json
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from url_shortener.models import Url
from url_shortener.tokenizer import Tokenizer


class UrlsView(APIView):
    def get(self, request, format=None):
        return Response({'urls': list(Url.objects.all().order_by('-creation_time').values())})

    def post(self, request, *args, **kwargs):
        token = Tokenizer().create_token(request.data['url'])
        return Response(json.dumps({
            'token': token,
        }))


def shortcut(request, token):
    url_item = get_object_or_404(Url, token=token)
    url_item.redirect_count += 1
    url_item.save()
    return redirect(url_item.url)


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        url_list = Url.objects.order_by('-id')
        context = {'url_list': url_list}
        return render(request, 'home.html', context)

    def post(self, request, *args, **kwargs):
        url = request.POST['url']
        if url:
            token = Tokenizer().create_token(url)
        return redirect('home')
