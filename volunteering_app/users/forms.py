from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("full_name",)
