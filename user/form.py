from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class createUserForm(UserCreationForm):
    email = forms.EmailField()
    department = forms.CharField(max_length=100)
    school = forms.CharField(max_length=200)
    name =forms.CharField(max_length=200)
    campus = forms.CharField(max_length=20)
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'department','school', 'name', 'campus', 'password1', 'password2']