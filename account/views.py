from django.shortcuts import render
from django.views.generic import DetailView

from .models import Profile
from .utils import DataMixin


class UserProfile(DataMixin, DetailView):
    model = Profile
    template_name = 'account/profile.html'
    pk_url_kwarg = 'profile_id'  # Replace 'id' to 'profile_id'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_context = self.get_user_context(get_types=False, get_menu=True, title=context['profile'])
        return dict(list(context.items()) + list(user_context.items()))
