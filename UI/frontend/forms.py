from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# form to create a new user
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']


# form to login
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)