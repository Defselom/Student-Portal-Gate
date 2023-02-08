
from django import forms
from django.forms import widgets
#pour les formulaires
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from . models import *



# class RegisterForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))

class youtubeform(forms.Form):
    text = forms.CharField( max_length=100, label="Enter Your YouTube Search : ")
    
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    