from django.contrib import admin
from . models import Issue, UserFeedback

# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    list_display=['staff', 'department', 'campus', 'fault_detection', 'date_reported']
class  UserFeedbackAdmin(admin.ModelAdmin):
    list_display = ['staff_name','feedback', 'fault_location', 'status']

admin.site.site_header = 'Estate and Works Admin'
admin.site.register(Issue, IssueAdmin)
admin.site.register(UserFeedback, UserFeedbackAdmin)