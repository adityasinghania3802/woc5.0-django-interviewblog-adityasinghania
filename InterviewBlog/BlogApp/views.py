# Create your views here.
from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
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

# @login_required(login_url='/login')
def homepage(request):
    post = BlogPost.objects.all()
    return render(request,'home.html',{'post':post})

# @login_required(login_url='/login')
def dashboard(request):
    # profile=list(Account.objects.filter(user=request.user).values('batch','program'))
    # batch = profile[0]['batch']
    # program = profile[0]['program']
    # params = {
    #     'batch' : batch,
    #     'program': program
    # }
    return render(request,'dashboard.html')

def addpost(request):
    if request.method=='POST':
            blog_title = request.POST.get('blog_title')
            company_name = request.POST.get('company_name')
            job_offer_type = request.POST.get('job_offer_type')        
            job_profile = request.POST.get('job_profile')        
            year = request.POST.get('year')   
            blog_content = request.POST.get('blog_content')   
            author=request.user
            update=BlogPost(blog_title=blog_title, company_name=company_name, job_offer_type=job_offer_type, job_profile=job_profile, year= year, blog_content=blog_content, author=author)
            update.save()
            messages.info(request, 'Your Entry has been Submitted!!')


    List=[]
    temp = BlogPost.CHOICES
    for i,j in temp:
        List.append(i)
    return render(request,'addpost.html',{'List':List})

def viewpost(request,pid):
    post=BlogPost.objects.get(post_id=pid)
    params = {'post':post}
    return render(request,'viewpost.html',params)

def search(request):
    searchresult=request.GET['search']
    if len(searchresult)>100:
        searchPosts= BlogPost.objects.none()
    else:
        searchPostsTitle = BlogPost.objects.filter(blog_title__icontains=searchresult)
        searchPostsContent = BlogPost.objects.filter(blog_content__icontains=searchresult)
        # searchPostsName = BlogPost.objects.filter(author__icontains=searchresult)
        searchPostsYear = BlogPost.objects.filter(year__icontains=searchresult)
        searchPostsCompany = BlogPost.objects.filter(company_name__icontains=searchresult)
        searchPosts=searchPostsTitle.union(searchPostsContent,searchPostsCompany,searchPostsYear)
    
    params = {'searchPosts' : searchPosts}
    return render(request, 'search.html', params)


def bookmarks(request,pid):
    post=BlogPost.objects.get(post_id=pid)
    
    # if post.bookmarks.filter(User=request.user.post_id).exists():
    #     post.bookmarks.remove(request.user)
    # else:
    post.bookmarks.add(request.user)
    messages.info(request, 'Added to Bookmarks Successfully!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def bookmarks_remove(request,pid):
    post=BlogPost.objects.get(post_id=pid)
    post.bookmarks.remove(request.user)
    messages.info(request, 'Removed from Bookmarks Successfully!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def bookmarkslist(request):
    list = BlogPost.objects.filter(bookmarks=request.user)
    return render(request, 'bookmarks.html', {'list': list})