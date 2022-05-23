from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from .enums import CurrencyChoices


class Ad(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False, verbose_name='Название')
    publication_date = models.DateField(auto_now_add=True, blank=False, null=False, verbose_name='Дата публикации')
    content = models.TextField(max_length=500, blank=False, null=False, verbose_name='Текст объявления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True, verbose_name='Фото')
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=True, verbose_name='Автор')
    type = models.ForeignKey('ItemType', on_delete=models.PROTECT, blank=False, null=False, verbose_name='Тип')
    price = models.FloatField(default=0, blank=False, null=True, verbose_name='Цена')
    currency = models.CharField(
        max_length=3,
        choices=CurrencyChoices.choices,
        default=CurrencyChoices.BYN,
        verbose_name='Валюта',
        blank=False,
        null=False,
    )
    is_sold = models.BooleanField(
        default=False,
        auto_created=False,
        verbose_name='Продано',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ad', kwargs={'ad_id': self.pk})

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['id']


class ItemType(models.Model):
    type = models.CharField(max_length=50, db_index=True, verbose_name='Тип товара')

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('type', kwargs={'type_id': self.pk})

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
        ordering = ['id']