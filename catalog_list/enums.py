from django.utils.translation import gettext_lazy as _
from django.db import models


class CurrencyChoices(models.TextChoices):
    BYN = 'BYN', _('р.')
    USD = 'USD', _('$')
    EUR = 'EUR', _('€')