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
        
class Image(models.Model):
    image = models.ImageField(upload_to = 'image')
    image_name= models.CharField(max_length=100)
    image_caption = models.CharField(max_length=500)
    profile = models.ForeignKey(Profile,on_delete= models.CASCADE)
    