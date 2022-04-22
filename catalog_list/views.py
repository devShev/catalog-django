from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, FormView

from .models import Ad, ItemType
from utils import DataMixin


class CatalogHome(DataMixin, ListView):
    model = Ad
    template_name = 'catalog_list/index.html'
    context_object_name = 'ads'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Каталог')

    def get_queryset(self):
        return Ad.objects.all().select_related('author', 'type')
