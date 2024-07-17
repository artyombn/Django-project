from django import forms
from .models import PreCoAuthor

class PreCoAuthorForm(forms.ModelForm):

    class Meta:
        model = PreCoAuthor
        exclude = ['user', 'idea']