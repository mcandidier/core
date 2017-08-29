from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'name': 'username',
                                       'placeholder': 'Username'}))
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control',
                                       'name': 'password',
                                       'placeholder': 'Password'}))
