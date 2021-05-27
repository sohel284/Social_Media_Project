from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from loginapp.models import UserProfile


class CreateNewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={
        'placeholder':'Enter your Email Address',
        'class': 'w-100 mt',
    }))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={
        'placeholder': 'Enter your username',
        'class': 'w-100 my-3',  
    }))
    password1 = forms.CharField(min_length=8, max_length=32, label="", required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'w-100',
    }))
    password2 = forms.CharField(min_length=8, max_length=32, label="", required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'w-100 my-3',
    }))
    class Meta:
        model = User
        fields = ('email','username','password1', 'password2', )


class UserProfileForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={
        'type':'Date', 
    }))
    class Meta:
        model = UserProfile
        exclude = ('user', )




