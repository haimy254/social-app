from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from .forms import ImageUploadForm
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Profile

# Create your views here.
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="accounts/register.html", context={"register_form":form})


        
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("all_images")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="accounts/login.html", context={"login_form":form})
 
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))  

        
@login_required(login_url='accounts/login')
def home(request):
    return render (request,'home')

@login_required(login_url='accounts/login')
def profile(request):
    if request.method == 'POST':
        user_form = NewUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profileform')
    else:
        user_form = NewUserForm(instance=request.user)
        form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', context={'profile_form':form} )
    
def home_view(request):
    return render(request,'home.html')

def profile_view(request):
    if request.method=="GET":
        profile=Profile.objects.filter();
       
      
    return render(request,'profile.html',{'profile':profile})
    
@login_required(login_url='accounts/login')
def display_images(request):
    if request.method=="GET":
        images=Image.objects.all();
        absolute_url=request.build_absolute_uri()
      
        return render(request,'show_images.html',{'all_images':images,"root_url":absolute_url})
 
@login_required(login_url='accounts/login.html')   
def add_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.save()
            return redirect('all_images')
    else:
        form = ImageUploadForm()
    return render(request, 'imageform.html', {'image_form' : form})
  
def success(request):
    return HttpResponse(request,'successfully uploaded')  


def get_update(request,image_id):
    the_id=int(image_id)
    
    try:
        image_sel=Image.objects.get(id=the_id)
        return render(request,'update_form.html',{'selected_image':image_sel})
    except:
        images=Image.objects.all()
        return render(request,'show_images.html',{'all_images':images})
    
def post_update(request,image_id):
    image_id= int(image_id)
    
    try:
        image_sel=Image.objects.post(id =image_id)
        image=Image(request.POST or None, instance=image_sel)
        if image.is_valid():
            image.save()
        return redirect('show_images.html',{'all_images':image})
    except Image.DoesNotExist:
        images=Image.objects.all()
        return redirect ('show_images.html',{'all_images':images})
    
@csrf_exempt
def search(request):   
    if request.method=='POST':
        search_term = request.POST.get("image_name")
       
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
    
@login_required(login_url='accounts/login')    
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
    
