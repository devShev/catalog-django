from django.db.models import Count

from catalog_list.models import *


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        types = ItemType.objects.all()

        context['types'] = types
        if 'type_selected' not in context:
            context['cat_selected'] = 0
        return context