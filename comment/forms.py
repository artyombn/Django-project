from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    text = forms.CharField(
        label='Comment text',
        # required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Write your comment here',
                'class': 'form-control',
                'rows': 5
            }
        )
    )


    class Meta:
        model = Comment
        fields = ('text',)
