from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CreateUserForm

from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Profile

# Create your views here.
def registerPage(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('home')
        
        
    context = {'form': form}
    return render(request,'register.html', context)
        
def login_user(request):
    form = Loginform()
    if request.method == "POST":
        form = Loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
    
    context={'form':form}
    return render (request,'home.html', context)
 
def logoutUser(request):
    logout(request)
    return redirect('login.html')  

        
@login_required(login_url='login.html')
def home(request):
    return render (request,'home')


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render (request,'profileform.html', context)
    
def home_view(request):
    return render(request,'home.html')