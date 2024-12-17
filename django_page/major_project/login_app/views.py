from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .models import *


@login_required
def Home(request):
    return render(request, 'login_app/index.html')

def RegisterView(request):
    if request.method== 'POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('password')
        
        user_data_has_error= False
        
        if User.objects.filter(email= email).exists():
            user_data_has_error=True
            messages.error(request,"Email already exists")
        
        if User.objects.filter(username= username).exists():
            user_data_has_error=True
            messages.error(request,"Username already exists")
        
        if len(password)<5:
            user_data_has_error= True
            messages.error(request, "Password must be at least 5 characters")
        
        if user_data_has_error:
            return redirect('register')
        else:
            new_user= User.objects.create_user(
                first_name= first_name,
                last_name= last_name,
                email=email,
                username= username,
                password= password
            )
            messages.success(request, "Account created. Login now")
            return redirect('login')
        
    return render(request, 'login_app/register.html')


def LoginView(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        
        user= authenticate(request, username= username, password= password) # this will take the username and password and check in database if any of them have the same username or password if it doesnot find the match then it returns None
        
        if user is not None:
            # log in user if credential are correct
            login(request,user)
            # redirect to home page
            return redirect('home')
        
        else:
            messages.error(request, "Invaild login details")
            return redirect('login')
        
        
    return render(request, 'login_app/login.html')


def LogoutView(request):
    logout(request)
    return redirect('login')

from login_app.models import doctor
@login_required
def DoctorsDetails(request):
    my_obj= doctor.objects.all()
    context= {'my_obj': my_obj}
    return render(request, 'login_app/doctors_details.html', context=context)

@login_required
def Hospitals(request):
    return render(request, 'login_app/hospitals.html')


@login_required
def UploadImage(request):
    if request.method == 'POST':
        uploaded_image = request.FILES['xray_image']
        # Save the image or process it as needed
        messages.success(request, "Image uploaded successfully!")
        return redirect('home')
    return render(request, 'login_app/index.html')

 
