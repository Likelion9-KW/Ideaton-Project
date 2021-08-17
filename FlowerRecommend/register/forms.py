from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.db.models.expressions import F
from django.forms import widgets
from .models import CustomUser



class MyAuthenticationForm(UserCreationForm):
    username=UsernameField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'nickname']
        widgets={
            'username':forms.TextInput(
                attrs={
                    'class':'id-input'
                }
            ),
            'password1':forms.PasswordInput(
                attrs={
                    'class':'password-input'
                }
            ),
            'password2':forms.PasswordInput(
                attrs={
                    'class':'password2-input'
                }
            ),
            'nickname':forms.TextInput(
                attrs={
                    'class':'nickname-input'
                }
            )

        }