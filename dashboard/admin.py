from django.contrib import admin
from . models import Issue

# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    list_display=['staff', 'department', 'campus', 'fault_detection', 'date_reported']


admin.site.site_header = 'Estate and Works Admin'
admin.site.register(Issue, IssueAdmin)