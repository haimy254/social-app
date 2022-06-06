from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo= models.ImageField(upload_to='profile/')
    bio = models.CharField(max_length=800)
    
   