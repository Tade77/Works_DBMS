from django.contrib import admin
from . models import Login, Issue

# Register your models here.
class LoginAdmin(admin.ModelAdmin):
    list_display = ['username']

class IssueAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'fault_detection', 'date_reported']
    
    
    admin.site.register(Login, LoginAdmin)
    admin.site.register(Issue)