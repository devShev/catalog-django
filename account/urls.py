from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('<int:profile_id>/', UserProfile.as_view() , name='profile'),
    path('<int:profile_id>/settings/', SettingsProfile.as_view(), name='settings'),
]
