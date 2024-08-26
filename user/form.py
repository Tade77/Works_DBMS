from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


CAMPUSES = [
    ('C1', 'Campus 1'),
    ('C2', 'Campus 2'),
]

class createUserForm(UserCreationForm):
    email = forms.EmailField()
    

    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']