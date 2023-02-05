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
from django.urls import reverse
from django.db.models import Max,Min

def index(request):
    if(request.user.is_authenticated):
        return redirect('home')
    else:
        return render(request,'index.html')

def registerpage(request):
    if(request.user.is_authenticated):
        return redirect('home')
    else:
        form=CreateUserForm(request.POST,request.FILES)
        if(request.method=="POST"):
            
            if form.is_valid():
                user=form.save()

                user.batch=request.POST.get('batch')
                user.program=request.POST.get('program')
                user.profile_pic=form.cleaned_data.get('profile_pic')
                print(user.profile_pic)
                update=Account(user=user)
                update.program=user.program
                update.batch=user.batch
                update.profile_pic=user.profile_pic
                update.save()
                messages.info(request, 'Account has been registered. Login to continue!!')
                return redirect('login')
        params={'form':form}
        return render(request,'register.html',params)

def loginpage(request):
    if(request.user.is_authenticated):
        return redirect('home')
    else: 
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

@login_required(login_url='/login')
def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login')
def homepage(request):
    post = BlogPost.objects.all()
    # for i in set:
    #     i.likecount = i.total_likes()
    #     print(i.likecount)
    # # post = BlogPost.objects.annotate(max_likes=Max('likecount')).order_by('-max_likes')
    # post = BlogPost.objects.all().order_by('-likecount')
    return render(request,'home.html',{'post':post})


@login_required(login_url='/login')
def dashboard(request):
    # profile=list(Account.objects.filter(user=request.user).values('batch','program'))
    # batch = profile[0]['batch']
    # program = profile[0]['program']
    # params = {
    #     'batch' : batch,
    #     'program': program
    # }
    return render(request,'dashboard.html')

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def viewpost(request,pid):
    post=BlogPost.objects.get(post_id=pid)
    # comments = get_object_or_404(Comment, BlogPost.post_id=pid)
    comments = Comment.objects.all()
    targetcomments =[]
    for i in comments:
        if i.postcomments.post_id==pid:
            targetcomments.append(i)

    liked_post = get_object_or_404(BlogPost, post_id=pid)
    total_likes = liked_post.total_likes()

    liked=False
    if liked_post.likes.filter(id=request.user.id).exists():
        liked=True

    bookmarked_post = get_object_or_404(BlogPost, post_id=pid)

    bookmarked=False
    if bookmarked_post.bookmarks.filter(id=request.user.id).exists():
        bookmarked=True

    params = {'post':post, 'targetcomments' : targetcomments, 'total_likes' : total_likes, 'liked' : liked, 'bookmarked' : bookmarked}
    return render(request,'viewpost.html',params)

@login_required(login_url='/login')
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
        searchPostsJobProfile = BlogPost.objects.filter(job_profile__icontains=searchresult)
        searchPostsJobOfferType = BlogPost.objects.filter(job_offer_type__icontains=searchresult)
        searchPosts=searchPostsTitle.union(searchPostsContent,searchPostsCompany,searchPostsYear,searchPostsJobProfile,searchPostsJobOfferType)
    
    params = {'searchPosts' : searchPosts}
    return render(request, 'search.html', params)

@login_required(login_url='/login')
def likes(request,pid):
    post = BlogPost.objects.get(post_id=pid)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('viewpost', args=[str(pid)]))

@login_required(login_url='/login')
def bookmarks(request,pid):
    post=BlogPost.objects.get(post_id=pid)
    
    if post.bookmarks.filter(id=request.user.id).exists():
        post.bookmarks.remove(request.user)
    else:
        post.bookmarks.add(request.user)
    return HttpResponseRedirect(reverse('viewpost', args=[str(pid)]))


@login_required(login_url='/login')
def bookmarkslist(request):
    list = BlogPost.objects.filter(bookmarks=request.user)
    return render(request, 'bookmarks.html', {'list': list})

@login_required(login_url='/login')
def editpost(request,pid):
    post = BlogPost.objects.get(post_id=pid)
    List=[]
    temp = BlogPost.CHOICES
    for i,j in temp:
        List.append(i)
    params ={'post' :post,
    'List' : List
    }
    return render(request, 'editpost.html', params)

@login_required(login_url='/login')
def editpostrecord(request,pid):
    if request.method == 'POST':
        title = request.POST['blog_title']
        name = request.POST['company_name']
        # offer_type = request.POST['job_offer_type']        
        profile = request.POST['job_profile']      
        year_ = request.POST['year']
        content = request.POST['blog_content']   
        record = BlogPost.objects.get(post_id=pid)
        record.blog_title = title
        record.company_name = name
        # record.job_offer_type = offer_type
        record.job_profile = profile
        record.year = year_
        record.blog_content = content
        record.save()
        messages.info(request, 'Your Entry has been Updated!!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required(login_url='/login')
def myblogs(request):
    author=request.user
    post = BlogPost.objects.filter(author=author)
    return render(request, 'myblogs.html', { 'post': post})

@login_required(login_url='/login')
def deletepost(request,pid):
    BlogPost.objects.filter(post_id=pid).delete()
    myblogs(request)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required(login_url='/login')
def addcomment(request, pid):
    if request.method=='POST':
            post = get_object_or_404(BlogPost, post_id=pid)
            name = request.POST.get('name')
            body = request.POST.get('body')
            update=Comment(name=name, body=body, postcomments=post)
            update.save()
            messages.info(request, 'Your Comment is added!!')
    return render(request, 'addcomment.html')

@login_required(login_url='/login')
def editprofile(request):
    user=request.user
    form = UpdateUserForm(initial={
        'first_name': user.first_name,
        'last_name' : user.last_name,
        'program':user.account.program,
        'batch' :user.account.batch,
        'profile_pic':user.account.profile_pic,
    })

    if(request.method=="POST"):
        
        form=UpdateUserForm(request.POST, request.FILES)
        if form.is_valid():
            
            user=request.user
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            batch = form.cleaned_data.get('batch')
            program = form.cleaned_data.get('program')
            profile_pic = form.cleaned_data.get('profile_pic')
            update = Account.objects.get(user=request.user)
            update.batch=batch
            update.program=program
            if 'profile_pic' in request.FILES:
                update.profile_pic = request.FILES['profile_pic']
            user.first_name=first_name
            user.last_name=last_name
            user.save()
            update.save()
            messages.info(request, 'Profile Updated!!')
            return redirect('dashboard')
    params={'form':form}
    return render(request,'editprofile.html',params)