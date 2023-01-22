# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate, login, logout
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
from .models import *
from .forms import *

def index(request):
    return render(request,'index.html')

def registerpage(request):
    form=CreateUserForm(request.POST)
    if(request.method=="POST"):
        
        if form.is_valid():
            user=form.save()
            user.batch=request.POST.get('batch')
            user.program=request.POST.get('program')
            update=Account(user=user)
            update.program=user.program
            update.batch=user.batch
            update.save()
            messages.info(request, 'Account has been registered. Login to continue!!')
            return redirect('login')
    params={'form':form}
    return render(request,'register.html',params)

def loginpage(request):
    
    if(request.method=="POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect ('dashboard')
        else:
            messages.info(request, 'Username or password is incorrect')
    params={}
    return render(request,'login.html',params)

def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login')
def homepage(request):
    return render(request,'home.html')

@login_required(login_url='/login')
def dashboard(request):
    profile=list(Account.objects.filter(user=request.user).values('batch','program'))
    batch = profile[0]['batch']
    program = profile[0]['program']
    params = {
        'batch' : batch,
        'program': program
    }
    return render(request,'dashboard.html', params)