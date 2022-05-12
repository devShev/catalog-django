from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import RegisterUserForm, LoginUserForm
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

        c_def = self.get_user_context(get_types=False, title='Связь с нами', cuurent_menu='contact')
        return dict(list(context.items()) + list(c_def.items()))


class Rules(DataMixin, TemplateView):
    template_name = 'catalog_list/rules.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(get_types=False, title='Правила площадки', cuurent_menu='rules')
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


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'catalog_list/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(get_types=False, get_menu=False, title='Регистрация')

        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'catalog_list/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(get_types=False, get_menu=False, title='Авторизация')

        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
