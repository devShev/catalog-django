from django.db.models import Count

from catalog_list.models import *

menu_list = [
    {'title': 'Каталог', 'url_name': 'home'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Правила', 'url_name': 'rules'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        types = ItemType.objects.all()
        context['types'] = types

        context['menu'] = menu_list.copy()
        if 'type_selected' not in context:
            context['type_selected'] = 0
        return context
