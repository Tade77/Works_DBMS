from django.db import models
from django.contrib.auth.models import User




SCHOOLS = [
    ('SC', 'school of science'),
    ('BIZ', 'business education'),
    ('ST', 'school of technical'),
    ('VC', 'vocation'),
    ('CE', 'continue education'),
    ('CM', 'computer'),
    ('FA', 'Art and fine Art'),
    ('EC', 'Early Childhood'),
    ('OR' ,'other'),
        
]
CAMPUSES = [
    ('C1', 'Campus 1'),
    ('C2', 'Campus 2'),
]
STATUS = [
    ('UA', 'Unattended'),
    ('PD', 'Pending'),
    ('RD', 'Rectified'),
]



class Login(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)
    
CAMPUSES = [
    ('C1' , 'campus1'),
    ('C2' , 'campus2'),
]
    
class Issue(models.Model):
        staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
        department = models.CharField(max_length=100)
        campus = models.CharField(max_length=10, choices=CAMPUSES, null=True)
        fault_detection = models.TextField(max_length=450,null=True)
        date_reported = models.DateTimeField(auto_now_add=True, editable=False)
        
        
class UserFeedback(models.Model):
    staff_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fault_location = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=10, choices=STATUS, null=True)
    feedback = models.TextField(max_length=200, null=True)
        
    

