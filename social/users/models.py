from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    profile_photo= models.ImageField(upload_to='profile/')
    bio = models.CharField(max_length=800)
    
    def __str__(self):
        return f'{self.user.username}profile'
    
class Comment(models.Model):
    comment = models.CharField(max_length=800, default='')
    
    def __str__(self):
        return self.comment
    
    def save_comment(self):
        self.save
        
class Image(models.Model):
    images = models.ImageField(upload_to = 'media/',default='')
    image_name= models.CharField(max_length=100)
    image_caption = models.CharField(max_length=500)
    profile = models.ForeignKey(Profile,on_delete= models.CASCADE)
    modified =models.DateTimeField(auto_now=True)
    comments=models.ManyToManyField('Comment', blank=True)
    likes = models.ManyToManyField(User, related_name='like_image')
    
    
    @classmethod
    def get_images(cls):
        images=cls.objects.all()
        return images
    
    @classmethod
    def filter_by_profile(cls,profile):
            images =cls.objects.filter(profile__id__icontains=profile).all()
            return images
        
    def __str__(self):
        return f'{self.profile.user.username} Post'