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
        hackathon = Hackathon.objects.get(id=1)
        context = {
            'hacker': hacker,
            'announcements': announcements,
            'sponsors': sponsors,
            'hackathon': hackathon,
        }
        return render(request, 'hacker/index.html', context)
        

    return render(request, 'hacker/index.html')



def announcement(request):
    user = request.user
    try:
        hacker = Hacker.objects.get(team_name=user)
    except:
        messages.error(request, 'You are not a hacker. Login as hacker!')
        return redirect('login')

    announcements = Announcement.objects.all()
    print(announcements)
    context = {
        'hacker': hacker,
        'announcements': announcements,
    }
    return render(request, 'hacker/announcement.html', context)


def sponsor(request):
    user = request.user
    try:
        hacker = Hacker.objects.get(team_name=user)
    except:
        messages.error(request, 'You are not a hacker. Login as hacker!')
        return redirect('login')

    sponsors = Sponsor.objects.all()
    context = {
        'hacker': hacker,
        'sponsors': sponsors,
    }
    return render(request, 'hacker/sponsor.html', context)

        
