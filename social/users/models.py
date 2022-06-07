from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo= models.ImageField(upload_to='profile/')
    bio = models.CharField(max_length=800)
    
class Comments(models.Model):
    comment = models.CharField(max_length=800, default='')
    
    def __str__(self):
        return self.comment
    
    def save_comment(self):
        self.save
        
class Likes(models.Model):
    # like = model
        pass
class Image(models.Model):
    images = models.ImageField(upload_to = 'image/',default='')
    image_name= models.CharField(max_length=100)
    image_caption = models.CharField(max_length=500)
    profile = models.ForeignKey(Profile,on_delete= models.CASCADE)
    comment = models.ForeignKey(Comments,on_delete= models.CASCADE )
    likes = models.ManyToManyField(User, related_name='like_image')
    