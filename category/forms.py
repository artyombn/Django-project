from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):

    title = forms.CharField(
        label='Category Title',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Input Category',
                'class': 'form-control',
            }
        )
    )
    description = forms.CharField(
        label='Description',
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Input Category Description here',
            }
        )
    )

    image = forms.ImageField(
        label='Image',
        required=False,
    )

    class Meta:
        model = Category
        fields = '__all__'
