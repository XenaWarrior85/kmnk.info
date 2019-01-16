from django import forms
from .models import Galery,Person
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    # Класс формы которая расширяет функционал админки и добавляет поля username и пароль
    # на страницу добавления и редактирования персоны
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password',)


class PersonForm(forms.ModelForm):
    # Класс формы для добавления персоны
    # проверить дублировнаие first name second name

    class Meta:
        model = Person
        fields = ( 'first_name', 'second_name', 'third_name', 'birthday', 'id')


class ImageForm(forms.ModelForm):
    # класс формы для добавления изображения персоны

    class Meta:
        model = Galery

        fields = ('image', 'id')


