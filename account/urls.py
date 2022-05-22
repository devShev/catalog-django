from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('<int:profile_id>/', UserProfile.as_view() , name='profile'),
]
