from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser

class  CustomUserCreationForm(UserCreationForm):
    model = (CustomUser)
    fields =  ('username','email','age',)

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username','email','age',)
