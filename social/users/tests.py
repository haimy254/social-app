from django.test import TestCase
import unittest
from .models import Profile,Image
# Create your tests here.
class ProfileTestClass(TestCase):
    '''tests for Category'''
    
    def setup(self):
        self.profile = Profile(bio ='this is bio', prophoto ='photo.jpg')    
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Profile))    
        
    def teardown(self):
        Profile.ojects.all().delete
        
    def test_save_method(self):
        self.profile.save()
        profile = Profile.get_post()      
        self.asserTrue(len(profile)>0) 
        
class ImageTestClass(TestCase):
    '''tests for Post(image) class'''
    
    def setUp(self):
                       
        self.post = Image(image = 'name.jpg', imagename='name', caption='caption is a caption', created ='date')        
    
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Image))  
        
    def test_save_method(self):
        self.post.save()
        post = Image.get_image()
        self.assertTrue(len(post)>0)        

class RegisterTestClass(unittest.TestCase):
    '''test for register class'''

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def test_if_can_register_profile(self):
        self.client.post('/users/register/', {
        'username': 'test1',
        # 'city': 'pavlodar',
        # 'phone': 87055551122,
        'password': 'Mypassword777',
        'password confirmation': 'Mypassword777'
    })
        self.assertTrue(Profile.objects.filter(user__username='test1').exists())

if __name__ == '__main__':
    unittest.main()