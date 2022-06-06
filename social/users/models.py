from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo= models.ImageField(upload_to='profile/')
    bio = models.CharField(max_length=800)
    
class Comments(models.Model):
    comment = models.CharField(max_length=800)
    
    def __str__(self):
        return self.comment
    
    def save_comment(self):
        self.save