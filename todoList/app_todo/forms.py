from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import AppUser


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ['email', 'password', 'full_name', 'contact']
        model = AppUser

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ["email", "password"]
        model = AppUser
