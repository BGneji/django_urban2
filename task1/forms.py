from django import forms
from django.contrib.auth.models import User

from django import forms
from django.core.exceptions import ValidationError


class UserRegister(forms.Form):
    username = forms.CharField(
        max_length=30,
        label="Введите логин",
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'})
    )
    password = forms.CharField(
        min_length=1,
        label="Введите пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
    )
    repeat_password = forms.CharField(
        min_length=1,
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'})
    )
    age = forms.CharField(
        max_length=3,
        label="Введите свой возраст",
        widget=forms.TextInput(attrs={'placeholder': 'Введите свой возраст'})
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password and repeat_password and password != repeat_password:
            raise forms.ValidationError("Пароли не совпадают.")

    def clean_age(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        if int(age) <= 18:
            raise forms.ValidationError('Возраст должен быть больше 18')
        return age
