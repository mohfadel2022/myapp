from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
    username = forms.CharField(required=True, 
                               widget=forms.TextInput(attrs={
                                   "class":"focus:outline-none", 'placeholder': 'Enter Username'
                                   }))
    email = forms.EmailField(required=True, 
                             widget=forms.EmailInput(attrs={
                                 "class":"focus:outline-none", 'placeholder': 'email@mail.com'
                                 }))
    password1 = forms.CharField(required=True, 
                                widget=forms.PasswordInput(attrs={
                                    "class":"focus:outline-none", 'placeholder': 'Enter Password'
                                    }))
    password2 = forms.CharField(required=True, 
                                widget=forms.PasswordInput(attrs={
                                    "class":"focus:outline-none", 'placeholder': 'Confirm Password'
                                    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

   