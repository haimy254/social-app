from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect ('base.html')
    else:
        messages.success('request',("The user is not registered"))
        return redirect ('authentication/registration.html')
    # return render(request,'authenticate/login.html')