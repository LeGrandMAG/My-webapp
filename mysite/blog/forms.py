from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=25)
    #email = forms.EmailField(label = 'Your email address')
    recipient = forms.EmailField(label = 'Recipient email')
    comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')