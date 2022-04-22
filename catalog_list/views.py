from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView

from .models import Ad, ItemType
from .utils import DataMixin


class CatalogHome(DataMixin, ListView):
    model = Ad
    template_name = 'catalog_list/index.html'
    context_object_name = 'ads'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Каталог', cuurent_menu='home')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Ad.objects.all().select_related('author', 'type')


def create(request):
    return HttpResponse("Создание записи")


class Contact(DataMixin, TemplateView):
    template_name = 'catalog_list/contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Связь с нами', cuurent_menu='contact')
        return dict(list(context.items()) + list(c_def.items()))


class Rules(DataMixin, TemplateView):
    template_name = 'catalog_list/rules.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Правила площадки', cuurent_menu='rules')
        return dict(list(context.items()) + list(c_def.items()))


class TypeView(DataMixin, ListView):
    model = Ad
    template_name = 'catalog_list/index.html'
    context_object_name = 'ads'
    allow_empty = False

    def get_queryset(self):
        return Ad.objects.filter(type__id=self.kwargs['ad_id']).select_related('type', 'author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        type = ItemType.objects.get(pk=self.kwargs['ad_id'])

        c_def = self.get_user_context(title=str(type.type), type_selected=type.pk, cuurent_menu='home')
        return dict(list(context.items()) + list(c_def.items()))
