# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.db import IntegrityError
#import user
from django.contrib.auth.models import User

# Create your views here.
def register(request):
        if request.method == "POST":
            username = request.POST["team_name"]
            email = request.POST["email"]
            password = request.POST["password"]
            
    
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
            except IntegrityError:
                messages.error(request, 'Team name already taken.')
                return redirect('register')
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login/register.html")
        

        
def land(request):
    return render(request, 'login/land.html')

def login(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(username, password, user)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, 'Invalid username and/or password.')
            return redirect('login')
    else:
        return render(request, "login/login.html")
    
    