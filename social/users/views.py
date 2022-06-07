from stringprep import in_table_c11_c12
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateUserForm
from .forms import UserUpdateForm, ProfileUpdateForm
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
        u_form= UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        
        if u_form.is_valid()and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {'u_form':u_form,
               'p_form':p_form}
    return render (request,'profile.html',context)
    
def home_view(request):
    return render(request,'home.html')

# def profile_view(request):
#     if request.method=="GET":
#         profile=Profile.objects.filter();
      
#         return render(request,'profile.html',{'proifle':profile})
    

def display_images(request):
    if request.method=="GET":
        Images=Image.objects.all();
      
        return render(request,'show_images.html',{'all_images':Images})
    
    
def image_view(request):
  
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'imageform.html', {'form' : form})
  
  
def success(request):
    return HttpResponse(request,'successfully uploaded')

@csrf_exempt
def search(request):   
    if request.method=='POST':
        search_term = request.POST.get("category")
       
        image_found_by_name=Image.objects.get(image_name=search_term)
        
        if image_found_by_name:
            found_images=image_found_by_name
            print(found_images)
            message = f"{search_term}" 
            
            return render(request, 'search.html',{"message":message,"images": found_images})  
        else:
            message="no such resource found"
            images=Image.objects.all()
            return render(request,'show_images.html',{"message":message,'all_images':images})
              
    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})