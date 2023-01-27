from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    program = models.CharField(max_length=100,default="")
    batch = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=100,default="Read my first post")
    blog_content = models.CharField(max_length=500,default="..")
    company_name = models.CharField(max_length=50,default="")
    CHOICES = (('Summer Internship','Summer Intership'),('Winter Internship Only','Winter Intership Only'),('Winter Intership & Job','Winter Internship & Job'),('Job Only','Job Only'))
    job_offer_type = models.CharField(max_length=100, choices=CHOICES,default="Job Only")
    job_profile = models.CharField(max_length=50,default="")
    year = models.IntegerField()
    # image = models.ImageField(upload_to="None")
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.blog_title + '|' + str(self.author)