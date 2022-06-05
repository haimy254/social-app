from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request,'authenticate/registration.html', context)
        
def login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect ('base.html')
#     else:
#         # messages.success('request',("The user is not registered"))
#         return redirect ('authentication/registration.html')
    return render(request,'authenticate/login.html')