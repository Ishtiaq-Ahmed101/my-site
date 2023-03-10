from django import forms
from djanggo.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
     