# urls for organiser

from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.index, name="h_index"),
    path("announcement/", views.announcement, name="h_announcement"),
   # path("hackthon/", views.hackathon_details, name="o_hackathon_details"),
   # path("sponsor/", views.sponsor_details, name="o_sponsor_details"),
    #path("team/", views.team_details, name="o_team_details"),
    
    
]