from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages
from .decorators import *

# Create your views here.

@unautheticated_user
def loginPage(request):
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('/')
                
            elif user_type == '2':
                return redirect('pharmacist_home')

            elif user_type == '3':
                return redirect('doctor_home')
            elif user_type == '4':
                return redirect('clerk_home')
            elif user_type == '5':
                return redirect('patient_home')
                
           
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            return redirect('login')
    
    return render(request,'login.html')



def logoutUser(request):
    logout(request)
    return redirect('login')
