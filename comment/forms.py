from django import forms
from .models import Comment, Idea, User

class CommentForm(forms.ModelForm):

    idea = forms.ModelChoiceField(
        queryset=Idea.objects.all(),
        empty_label='Select Idea',
        # required = False,  # запрещено на уровне модели
    )

    author = forms.ModelChoiceField(
        queryset=User.objects.all(),
        empty_label='Select author',
    )

    text = forms.CharField(
        label='Comment text',
        # required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Write your comment here',
            }
        )
    )


    class Meta:
        model = Comment
        fields = '__all__'
