from django.contrib import admin

# Register your models here.
from url_shortener.models import Url


class UrlAdmin(admin.ModelAdmin):
    list_display = ('url', )
    search_fields = ('url', )


admin.site.register(Url, UrlAdmin)
