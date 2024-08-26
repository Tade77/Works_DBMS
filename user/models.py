from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    department = models.CharField(max_length=100, null=True)
    phone= models.CharField(max_length=12, null=True)
    campus = models.CharField(max_length=10, null=True)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_images')
    
    def __str__(self):
        return f'{self.staff.username} - profile'
