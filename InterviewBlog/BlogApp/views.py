from django.shortcuts import render
def index(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')
# Create your views here.
