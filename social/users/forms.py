from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Image, Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class Loginform(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo','bio']
        templates = ('profileform.html')
        
class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ['images','image_name','image_caption']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']