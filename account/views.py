from django.contrib.auth import login, logout

from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView


from .forms import RegisterUserForm, LoginUserForm, ProfileEditForm
from .models import Profile
from .utils import DataMixin, NonLoginRequiredMixin
from catalog_list.models import Ad


class RegisterUser(NonLoginRequiredMixin, DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_context = self.get_user_context(get_types=False, get_menu=False, title='Регистрация')

        return dict(list(context.items()) + list(user_context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('home')


class LoginUser(NonLoginRequiredMixin, DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'account/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_context = self.get_user_context(get_types=False, get_menu=False, title='Авторизация')

        return dict(list(context.items()) + list(user_context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


class UserProfile(DataMixin, DetailView):
    model = Profile
    template_name = 'account/profile.html'
    pk_url_kwarg = 'profile_id'  # Replace 'id' to 'profile_id'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_context = self.get_user_context(get_types=False, get_menu=True, title=context['profile'])
        user_context['ads'] = Ad.objects.filter(author__profile=context['profile'])
        return dict(list(context.items()) + list(user_context.items()))


class SettingsProfile(DataMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'account/profile_settings.html'
    pk_url_kwarg = 'profile_id'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if context['profile'].user.pk != self.request.user.pk:
            return HttpResponseForbidden()
        print('OK!')
        user_context = self.get_user_context(get_types=False, get_menu=True, title='Изменение профиля')
        return dict(list(context.items()) + list(user_context.items()))

    def form_valid(self, form):
        if form.instance.user != self.request.user:
            return HttpResponseForbidden()
        return super().form_valid(form)