from django.forms import ModelForm,TextInput, EmailInput, NumberInput, PasswordInput
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
        # fields ='__all__'
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: auto;',
                'placeholder': 'UserName'
                }),
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: auto;',
                'placeholder': 'First Name'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: auto;',
                'placeholder': 'Last Name'
                }),
            'program': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: auto;',
                'placeholder': 'Program'
                }),
            'batch': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: auto;',
                'placeholder': 'Batch'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: auto;',
                'placeholder': 'Email'
                }),
            
            'password1': PasswordInput(attrs={
                'class': "form-control", 
                'style': 'max-width: auto;',
                'placeholder': 'Password'
                }),
            'password2': PasswordInput(attrs={
                'class': "form-control", 
                'style': 'max-width: auto;',
                'placeholder': 'Confirm Password'
                }),
        }


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
        widgets ={
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: auto;',
                'placeholder': 'First Name'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: auto;',
                'placeholder': 'Last Name'
                }),
            'program': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: auto;',
                'placeholder': 'Program'
                }),
            'batch': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: auto;',
                'placeholder': 'Batch'
                }),
        }
