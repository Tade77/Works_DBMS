from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


CAMPUSES = [
    ('C1', 'Campus 1'),
    ('C2', 'Campus 2'),
]

class createUserForm(UserCreationForm):
    email = forms.EmailField()
    department = forms.CharField(max_length=100)
    school = forms.CharField(max_length=200)
    campus = forms.MultipleChoiceField(choices=CAMPUSES)
    phone = forms.CharField(max_length=11)
    firstname = forms.CharField(max_length=200)
    lastname = forms.CharField(max_length=200)
    
    class Meta:
        model = User
        fields = ['firstname', 'lastname','email', 'phone' ,'department','school', 'username', 'campus', 'password1', 'password2']