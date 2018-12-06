from django.contrib import admin

# Register your models here.
from url_shortener.models import Url


class UrlAdmin(admin.ModelAdmin):
    pass


admin.site.register(Url, UrlAdmin)
