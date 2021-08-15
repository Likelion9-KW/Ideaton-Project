from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class MyAuthenticationForm(AuthenticationForm):

    username = UsernameField(
        label=("ID"))
    password = forms.CharField(
        label=("Password"),
        strip=False,
    )
