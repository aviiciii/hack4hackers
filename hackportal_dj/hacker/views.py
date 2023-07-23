from django.shortcuts import render
#i
#from .models import Sponsor
from organiser.models import Hackathon, Sponsor
from login.models import Hacker, Organiser

def index(request):
    return render(request, 'hacker/index.html')



#def sponsor_details(request):
    return render(request, 'hacker/sponsor_details.html')

#def team_details(request):
    return render(request, 'hacker/team_details.html')
