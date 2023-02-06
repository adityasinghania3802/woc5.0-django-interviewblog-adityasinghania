from django.db import models
from django import forms
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    program = models.CharField(max_length=100,default="")
    batch = models.IntegerField(default=0)
    profile_pic = models.ImageField(upload_to = "BlogApp/images", null =True, blank = True)

    def __str__(self):
        return self.user.username

class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=100,default="Read my first post")
    blog_content = RichTextField(blank=True, null=True)
    company_name = models.CharField(max_length=50,default="")
    CHOICES = (('Summer Internship','Summer Intership'),('Winter Internship Only','Winter Intership Only'),('Winter Internship & Job','Winter Internship & Job'),('Job Only','Job Only'))
    job_offer_type = models.CharField(max_length=100, choices=CHOICES, default="Job Only")
    job_profile = models.CharField(max_length=50,default="")
    year = models.IntegerField()
    # image = models.ImageField(upload_to="None")
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    bookmarks = models.ManyToManyField(User, default=None, blank=True, related_name='bookmarks')
    likes = models.ManyToManyField(User, default=None, blank=True, related_name='likes')
    post_date = models.DateField(auto_now_add=True)
    # likecount = models.IntegerField(default=0)

    def __str__(self):
        return self.blog_title + '|' + str(self.author)

    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    postcomments = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='postcomments', default=None)
    name = models.CharField(max_length=50, default="Anonymous")
    body = models.TextField()

    def __str__(self):
        return self.postcomments.blog_title + '|' + str(self.name)