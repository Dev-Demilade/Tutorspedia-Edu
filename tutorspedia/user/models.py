from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.png', upload_to='profile_images')
    bio = models.TextField()
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save()
        
        img = Image.open(self.avatar.path)
        
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
        
    

# Create your models here.
