from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
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
            user = form.cleaned_data.get('username')
            messages.success(request,'account was created for'+ user)
            return redirect('login')
        
        
    context = {'form': form}
    return render(request,'accounts/register.html', context)
        
def login(request):
    form = Loginform()
    if request.method == "POST":
        form = Loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                form = login(request, user)
                messages.success(request, f' wecome {username} !!')
                return redirect('register')
            else:
                messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render (request,'home.html',{'form':form})
 
def logout(request):
    
    return redirect(request,'login.html')  

        
@login_required(login_url='account/login.html')
def home(request):
    return render (request,'home')

@login_required(login_url='login.html')
def profile(request):
    if request.method == 'POST':
        u_form= UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        
        if u_form.is_valid()and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {'u_form':u_form,
               'p_form':p_form}
    return render (request,'profile.html',context)
    
def home_view(request):
    return render(request,'home.html')

def profile_view(request):
    if request.method=="GET":
        profile=Profile.objects.filter();
      
        return render(request,'profile.html',{'proifle':profile})
    
@login_required(login_url='account/login.html')
def display_images(request):
    if request.method=="GET":
        Images=Image.objects.all();
        absolute_url=request.build_absolute_uri()
      
        return render(request,'show_images.html',{'all_images':Images,"root_url":absolute_url})
 
@login_required(login_url='account/login.html')   
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
    
def delete_image(request,image_id):
    the_id=int(image_id)
    images=0

    try:
        image_sel=Image.objects.get(id=the_id)
        image_sel.delete()
        images=Image.objects.all()
        return render(request,'show_images.html',{'all_images':images})
    except:
        images=Image.objects.all()
        return render(request,'show_images.html',{'all_images':images})