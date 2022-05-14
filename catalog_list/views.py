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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_context = self.get_user_context(title='Каталог', cuurent_menu='home')
        return dict(list(context.items()) + list(user_context.items()))

    def get_queryset(self):
        return Ad.objects.all().select_related('author', 'type')


class DetailAd(DataMixin, DetailView):
    model = Ad
    template_name = 'catalog_list/ad.html'
    pk_url_kwarg = 'ad_id' # Replace 'id' to 'ad_id'
    context_object_name = 'ad'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_context = self.get_user_context(get_types=False, get_menu=True, title=context['ad'])
        return dict(list(context.items()) + list(user_context.items()))


class TypeView(DataMixin, ListView):
    model = Ad
    template_name = 'catalog_list/index.html'
    context_object_name = 'ads'
    allow_empty = False

    def get_queryset(self):
        return Ad.objects.filter(type__id=self.kwargs['type_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        type = ItemType.objects.get(pk=self.kwargs['type_id'])

        user_context = self.get_user_context(title=str(type.type), type_selected=type.pk, cuurent_menu='home')
        return dict(list(context.items()) + list(user_context.items()))


def create(request):
    return HttpResponse("Создание записи")


# TODO
class Contact(DataMixin, TemplateView):
    template_name = 'catalog_list/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_context = self.get_user_context(get_types=False, title='Связь с нами', cuurent_menu='contact')
        return dict(list(context.items()) + list(user_context.items()))


# TODO
class Rules(DataMixin, TemplateView):
    template_name = 'catalog_list/rules.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(get_types=False, title='Правила площадки', cuurent_menu='rules')
        return dict(list(context.items()) + list(user_context.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'catalog_list/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_context = self.get_user_context(get_types=False, get_menu=False, title='Регистрация')

        return dict(list(context.items()) + list(user_context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'catalog_list/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_context = self.get_user_context(get_types=False, get_menu=False, title='Авторизация')

        return dict(list(context.items()) + list(user_context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
