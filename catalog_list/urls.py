from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', CatalogHome.as_view(), name='home'),
    path('ad/<int:ad_id>/', DetailAd.as_view(), name='ad'),
    path('type/<int:type_id>/', TypeView.as_view(), name='type'),
    path('search/', SearchResult.as_view(), name='search'),
    path('create/', create, name='create'),
    path('contact/', Contact.as_view(), name='contact'),
    path('rules/', Rules.as_view(), name='rules'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
