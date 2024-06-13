from django import forms
from .models import Idea, Category, User

class IdeasForm(forms.ModelForm):

    title = forms.CharField(
        label='Idea Title',
        # initial='New Idea',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Input Idea',
                'class': 'form-control',
            }
        )
    )
    description = forms.CharField(
        label='Description',
        # initial='Idea description',
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Input Description here',
            }
        )
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Select category',
        # required = False,  # запрещено на уровне модели
    )

    author = forms.ModelChoiceField(
        queryset=User.objects.all(),
        empty_label='Select author',
    )

    class Meta:
        model = Idea
        fields = '__all__'
