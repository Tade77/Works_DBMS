from django.test import TestCase
from . models import Issue
from django.contrib.auth.models import User
# Create your tests here.
    
class TestIssue(TestCase):
    def test_should_create_user(self):
        staff = User.objects.create(id="1",username= "ade" ,email="cce@gmail.com")
        staff.set_password('12345')
        staff.save()
        issue = Issue(staff=User, department="cce", campus="campus1",fault_detection="low voltage",)
        issue.save()
        
        self.assertEqual(str(issue),"low voltage")