from django.db import models
from django.utils import timezone


class Url(models.Model):
    url = models.URLField(
        verbose_name='Ссылка',
        max_length=2048
    )
    token = models.CharField(
        max_length=8,
        help_text='Сокращенная ссылка',
        unique=True
    )
    creation_time = models.DateTimeField(
        verbose_name='Дата создания',
        default=timezone.now
    )
    redirect_count = models.IntegerField(
        verbose_name='Количество переходов по ссылке',
        default=0
    )
