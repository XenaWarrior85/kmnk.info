from django import forms
from .models import Galery,Person
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    # Добавление формы юзера
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password',)


class PersonForm(forms.ModelForm):
    # Добавление формы персоны

    class Meta:
        model = Person
        fields = ( 'first_name', 'second_name', 'third_name', 'birthday', 'id')


class ImageForm(forms.ModelForm):
    # Добавление формы фото

    class Meta:
        model = Galery

        fields = ('image', 'id')


