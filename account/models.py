from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User ID')
    location = models.CharField(max_length=20, null=True, blank=True, verbose_name='Населённый пункт')
    photo = models.ImageField(upload_to='avatars/%Y/%m/%d/', null=True, blank=True, verbose_name='Фото')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'profile_id': self.pk})