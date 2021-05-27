from django import forms
from django import forms
from postapp.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption', ]

