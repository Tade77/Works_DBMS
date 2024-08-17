from django.contrib import admin
from . models import Login, Register, Issue

# Register your models here.
class LoginAdmin(admin.ModelAdmin):
    list_display = ['username']

class RegisterAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'school', 'campus', 'department', 'email']

class IssueAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'fault_detection', 'date_reported']
    
    
    admin.site.register(Login, LoginAdmin)
    admin.site.register(Register, RegisterAdmin)
    admin.site.register(Issue)