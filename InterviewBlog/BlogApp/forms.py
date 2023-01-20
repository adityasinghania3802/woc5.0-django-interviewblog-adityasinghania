from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm  
from django import forms
from django.contrib.auth.models import User 

class CreateUserForm(UserCreationForm):
    program = forms.CharField(label='Program')
    batch = forms.IntegerField(label='Batch')
    class Meta:
        model = User
        fields = ['username','email','program','batch','password1','password2']