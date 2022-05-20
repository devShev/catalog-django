from django.contrib.auth.mixins import AccessMixin

from catalog_list.models import *

menu_list = [
    {'title': 'Каталог', 'url_name': 'home'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Правила', 'url_name': 'rules'},
]


class DataMixin:
    def get_user_context(self, get_types=True, get_menu=True, **kwargs):
        context = kwargs

        if get_types:
            types = ItemType.objects.all()
            context['types'] = types

        if get_menu:
            context['menu'] = menu_list.copy()

        if 'type_selected' not in context:
            context['type_selected'] = 0

        return context


class NonLoginRequiredMixin(AccessMixin):
    """Verify that the current user is not authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
