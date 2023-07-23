from django.shortcuts import render
from .models import Hackathon, Sponsor

# import messages
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'organiser/index.html')


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

        messages.success(request, 'Announcement added successfully!')
        
        return render(request, 'organiser/announcement.html')

    return render(request, 'organiser/announcement.html')