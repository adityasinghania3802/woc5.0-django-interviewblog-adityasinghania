from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm  
from django import forms
from django.contrib.auth.models import User 

class CreateUserForm(UserCreationForm):
    program = forms.CharField(label='Program',required=True)
    batch = forms.IntegerField(label='Batch',required=True)
    profile_pic = forms.ImageField(label="Upload Profile Pic - ", required=False)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','program','batch','password1','password2','profile_pic']


# class CreateBlogPost(UserCreationForm):
#     blog_title = forms.CharField(label='Title')
#     company_name = forms.CharField(label="Company Name")
#     year = forms.IntegerField(label='Year')
#     job_profile = forms.CharField(label = 'Job Profile')
#     job_offer_type = forms.CharField(label='Job Offer Type')
#     blog_content = forms.CharField(label='Content')

class UpdateUserForm(forms.ModelForm):
     program = forms.CharField(label='Program',required=True)
     batch = forms.IntegerField(label='Batch',required=True)
     profile_pic = forms.ImageField(label="Upload Profile Pic - ", required=False)
     class Meta:
        model = User
        fields = ['first_name','last_name','program','batch','profile_pic']
