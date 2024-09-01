from django.contrib import admin
from .models import Profile
# Register your models here.

class  ProfileAdmin(admin.ModelAdmin):
    list_display = ['staff', 'department', 'phone', 'campus']

admin.site.register(Profile, ProfileAdmin)
