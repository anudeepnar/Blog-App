from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']

        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password'
        }