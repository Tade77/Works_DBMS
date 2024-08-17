from django.db import models




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
DEPARTMENTS = [
    ('EW', 'Estate and works'),
    ('AD', 'Admin block'),
    ('ST', 'Student Affairs'),
    ('RG', 'Registry'),
    ('TH', 'Theatre Hall'), 
    ('BS', 'Bursary'),
    ('LB', 'Library'),
    ('PP', 'Physical Planning'),
    ('PD', 'Physics DP'),
    ('CH', 'Chemistry DP'),
    ('PL', 'Physics Lab'),
    ('CL', 'Chemistry Lab')
    
    
]
CAMPUSES = [
    ('C1', 'Campus 1'),
    ('C2', 'Campus 2'),
]




class Login(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)
    
class Register(models.Model):
    name = models.CharField(max_length=150, unique=True)
    username = models.CharField(max_length=100, unique=True)
    school = models.CharField(max_length=200, unique=True, choices=SCHOOLS)
    campus = models.CharField(max_length=20,unique=True, choices=CAMPUSES)
    department = models.CharField(max_length=100, unique=True, choices=DEPARTMENTS)
    email= models.EmailField(("email"), max_length=200, unique=True)
    password = models.CharField(max_length=100, unique=True)
    confirm_password = models.CharField(max_length=100, unique=True)
    
class Issue(models.Model):
        name = models.CharField(max_length=100, unique=True)
        department = models.CharField(max_length=100)
        fault_detection = models.TextField(max_length=500,unique=True)
        date_reported = models.DateTimeField(auto_now_add=True)

