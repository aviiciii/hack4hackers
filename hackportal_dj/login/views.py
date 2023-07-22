# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.db import IntegrityError
#import user
from django.contrib.auth.models import User
from .models import Hacker, Organiser

# Create your views here.
def register_view(request):
        if request.method == "POST":
            username = request.POST["team_name"]
            email = request.POST["email"]
            password = request.POST["password"]
            name1 = request.POST["name1"]
            name2 = request.POST["name2"]
            name3 = request.POST["name3"]
            try:
                user = User.objects.create_user(username, email, password)
                user.save()

                hacker = Hacker(team_name=username, lead_name=name1, lead_email=email, member1_name=name2, member2_name=name3)
                hacker.save()
            


            except IntegrityError:
                messages.error(request, 'Team name already taken.')
                return redirect('register')
            messages.success(request, 'Team registered successfully!')
            return redirect('land')
        else:
            return render(request, "login/register.html")
        

        
def land(request):
    return render(request, 'login/land.html')

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(username, password, user)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            # check if user is superuser
            
            if user.is_superuser:
                return redirect('o_index')
            else:
                return redirect('h_index')
        else:
            messages.error(request, 'Invalid username and/or password.')
            return redirect('login')
    else:
        return render(request, "login/login.html")
    
    