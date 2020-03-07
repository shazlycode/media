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

    def clean_username(self):
        cd=self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('This user is already registered')
        return cd['username']

    def clean_password2(self):
        cd= self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('password confirmation is not correct')
        return cd['password2']


class LogForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username', 'password')

    