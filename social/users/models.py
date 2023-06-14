from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE, blank=True)
    avatar= models.ImageField(upload_to='profile_avators', default='')
    bio = models.CharField(max_length=800)
    email = models.EmailField(max_length= 30,null=True)
    # number = Phone()
    
    def __str__(self):
        return self.user.username
        
    
    def save_profile(self):
        self().save()

        #  # # resize image
        avator = Image.open(self.avatar.path) # Open image
        if avator.height > 300 or avator.width > 300:
            output_size = (300, 300)
            avator.thumbnail(output_size) # Resize image
            avator.save(self.avatar.path) # Save it again and override the larger image
    
class Comment(models.Model):
    comment = models.CharField(max_length=800, default='')
    
    def __str__(self):
        return self.comment
    
    def save_comment(self):
        self.save
        
class Image(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE, blank=True)
    images = models.ImageField(upload_to = 'media/',default='')
    image_name= models.CharField(max_length=100)
    image_caption = models.CharField(max_length=500)
    modified =models.DateTimeField(auto_now=True)
    comments=models.ManyToManyField('Comment', blank=True)
    likes = models.ManyToManyField(User, related_name='like_image')

    def save_comment(self):
        self.save
    
    
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