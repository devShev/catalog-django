from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from account.models import Profile


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]


# class DateInput(forms.DateInput):
#     input_type = 'date'


class ProfileEditForm(forms.ModelForm):
    photo = forms.ImageField(required=False, label='Фото профиля', widget=forms.FileInput(attrs={'class': 'form-control'}))
    location = forms.CharField(required=False, label='Населённый пункт', widget=forms.TextInput(attrs={'class': 'form-control col-lg-4 themed-grid-col'}))
    birth_date = forms.DateField(required=False, label='Дата рождения', widget=forms.DateInput(attrs={'class': 'form-control col-lg-4 themed-grid-col'}))
    phone_number = forms.CharField(required=False, label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control col-lg-4 themed-grid-col'}))
    telegram = forms.CharField(required=False, label='Telegram', widget=forms.TextInput(attrs={'class': 'form-control col-lg-4 themed-grid-col'}))


    class Meta:
        model = Profile
        fields = [
            'photo',
            'location',
            'birth_date',
            'phone_number',
            'telegram',
        ]