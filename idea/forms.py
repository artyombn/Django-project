from django import forms
from .models import Idea, Category, User

class IdeasForm(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ('title', 'description', 'category', 'image')

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
    )

    image = forms.ImageField(
        label='Image',
        required=False,
    )


    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super(IdeasForm, self).__init__(*args, **kwargs)
        if request:
            self.fields['author'].initial = request.user
            self.fields['author'].widget = forms.HiddenInput()
