from  django import forms
from . models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['staff', 'department', 'campus', 'fault_detection', 'date_reported']