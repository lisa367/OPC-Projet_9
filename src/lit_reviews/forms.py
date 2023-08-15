from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from reviews_app.models import UserFollows


class LoginForm(AuthenticationForm):
    pass
    # model = User
    # fields = ["username", "password"]


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
        ]


class NewSubscriptionForm(forms.Form):
    # user_to_follow = forms.CharField(widget=forms.TextInput, label=None, attrs={"name":"username", "class": "user-to-follow", "placeholder":"Nom d'utilisateur"})
    user_to_follow = forms.CharField(widget=forms.TextInput, label=None)
