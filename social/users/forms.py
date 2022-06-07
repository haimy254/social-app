from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Image, Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo','bio']
        templates = ()
        
class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ['images','image_name','image_caption',]