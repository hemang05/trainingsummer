from django import forms
from django.contrib.auth.models import User

class Signup(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','password','email']
