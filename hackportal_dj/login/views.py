# Create your views here.
from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'login/login.html')
    

def register(request):
    return render(request, 'login/register.html')

def land(request):
    return render(request, 'login/land.html')