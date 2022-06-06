from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CreateUserForm

# Create your views here.
def registerPage(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
            return redirect('authenticate/login.html')
        
        
    context = {'form': form}
    return render(request,'authenticate/register.html', context)
        
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('home.html')
        else:
            messages.info('request',"The username or password is incorrect")
    return render (request,'authenticate/login.html')
    

def home(request):
    return render (request,'home')