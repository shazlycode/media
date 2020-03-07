from django import forms
from django.contrib.auth.models import User
from django.db import models
class RegisterForm(forms.ModelForm):
    class Meta:
        model= User
        fields=('username', 'password1','password2', 'first_name', 'last_name', 'email')
    username=forms.CharField(max_length=100, label='Username')
    first_name=forms.CharField(max_length=100, label='First Name')
    last_name= forms.CharField(max_length=100, label='Last Name')
    email= forms.EmailField(max_length='100', label='Email')
    password1 = forms.CharField(label=("Password"),
    widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password confirmation"),
    widget=forms.PasswordInput,
    help_text=("Enter the same password as above, for verification."))