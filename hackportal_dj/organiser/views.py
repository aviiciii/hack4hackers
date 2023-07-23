from django.shortcuts import render
from .models import Hackathon, Sponsor, Announcement
from login.models import Hacker, Organiser


# import messages
from django.contrib import messages

# import datetime
from datetime import datetime
from hacker.models import Doubt
# Create your views here.


def index(request):

    # get all hackers
    count_hackers = len(Hacker.objects.all()) * 3

    count_organisers = len(Organiser.objects.all())

    count_announcements = len(Announcement.objects.all())

    context={
        'count_hackers': count_hackers,
        'count_organisers': count_organisers,
        'count_announcements': count_announcements,
    }

    return render(request, 'organiser/index.html', context=context)


def hackathon_details(request):

    if request.method == 'POST':
        form = request.POST

        name = form['hackathon_name']
        start_date = form['start_date']
        end_date = form['end_date']
        location = form['venue']
        duration = form['duration']
        theme = form['theme']
        description = form['description']
        eligibility = form['eligibility']
        team_size = form['team_size']
        prizes = form['prizes']
        
        try:
            hackathon = Hackathon.objects.get(id=1)
            hackathon.name = name
            hackathon.start_date = start_date
            hackathon.end_date = end_date
            hackathon.location = location
            hackathon.duration = duration
            hackathon.theme = theme
            hackathon.description = description
            hackathon.eligibility = eligibility
            hackathon.team_size = team_size
            hackathon.prizes = prizes
            
        except Hackathon.DoesNotExist:
            hackathon = Hackathon(name=name, start_date=start_date, end_date=end_date, location=location, duration=duration, theme=theme, description=description, eligibility=eligibility, team_size=team_size, prizes=prizes)

        hackathon.save()

        messages.success(request, 'Hackathon details saved successfully!')
        

        return render(request, 'organiser/hackathon_details.html')

    return render(request, 'organiser/hackathon_details.html')


def sponsor_details(request):
    
    if request.method == 'POST':
        form = request.POST

        name = form['name']
        description = form['description']
        website = form['website']
       
        sponsor = Sponsor(name=name, description=description, website=website)

        sponsor.save()

        messages.success(request, 'Sponsor added successfully!')
        
        return render(request, 'organiser/sponsor_details.html')


    return render(request, 'organiser/sponsor_details.html')


def announcement(request):

    if request.method=='POST':
        form = request.POST

        title = form['title']
        description = form['description']
        category = form['category']

        try:
            announcement = Announcement(title=title, description=description, category=category, date=datetime.now())
            announcement.save()
        except:
            messages.error(request, 'Error in adding announcement!')
        else:   
            messages.success(request, 'Announcement added successfully!')
        
        return render(request, 'organiser/announcement.html')

    return render(request, 'organiser/announcement.html')


def doubts(request):
    hacker_doubts = Doubt.objects.all()
    context = {
        'doubts': hacker_doubts,
    }


    return render(request, 'organiser/doubts.html', context=context)


