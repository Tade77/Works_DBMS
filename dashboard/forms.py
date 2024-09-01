from  django import forms
from . models import Issue, UserFeedback


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['staff', 'department', 'campus', 'fault_detection']
        
        
class UserFeedBackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields= ['staff_name', 'feedback', 'status', 'fault_location']