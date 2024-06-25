from django import forms
from django.contrib.auth.forms import UserCreationForm

from idea.models import Idea
from .models import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your username',
                'class': 'form control',
            }
        )
    )
    first_name = forms.CharField(
        label='First name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your first name',
                'class': 'form control',
            }
        )
    )
    last_name = forms.CharField(
        label='Surname',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your surname',
                'class': 'form control',
            }
        )
    )
    age = forms.IntegerField(
        label='Age',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your age',
                'class': 'form control',
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your email',
                'class': 'form control',
            }
        )
    )
    avatar = forms.ImageField(
        label='Avatar',
        widget=forms.FileInput,
    )


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'age', 'email', 'avatar')