from xml.etree.ElementTree import Comment
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from .models import Image, Profile

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ('username','email','password1','password2')

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
        
class Loginform(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
        
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar','bio','email']
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
        
# class CommentForm(forms.ModelForm):
    
#     class Meta:
#         model = Comment
#         fields = ['user', 'comment']