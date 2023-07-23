from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
# messages
from django.contrib import messages

from login.models import Hacker, Organiser
from organiser.models import Announcement, Sponsor, Hackathon

def index(request):
    user = request.user
    try:
        hacker = Hacker.objects.get(team_name=user)
    except:
        messages.error(request, 'You are not a hacker. Login as hacker!')
        return redirect('login')
    if user.is_authenticated and hacker:
        announcements = Announcement.objects.all()
        sponsors = Sponsor.objects.all()
        hackathons = Hackathon.objects.all()
        context = {
            'hacker': hacker,
            'announcements': announcements,
            'sponsors': sponsors,
            'hackathons': hackathons,
        }
        return render(request, 'hacker/index.html', context)
        

    return render(request, 'hacker/index.html')



#def sponsor_details(request):
    return render(request, 'hacker/sponsor_details.html')

#def team_details(request):
    return render(request, 'hacker/team_details.html')
