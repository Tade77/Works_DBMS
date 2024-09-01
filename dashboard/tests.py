from django.test import TestCase
from . models import Login, Issue, UserFeedback

# Create your tests here.
class TestLoginModel(TestCase):
    def test_user_login(self):
        user= Login.objects.get(username="kunle", password="kunle")
        # user.set_password("12345")
        user.save()
        self.assertEqual(str(user), 'kunle')
        
