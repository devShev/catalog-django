from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', CatalogHome.as_view(), name='home'),
    path('create/', create, name='create'),
    path('contact/', Contact.as_view(), name='contact'),
    path('rules/', Rules.as_view(), name='rules'),
]
