# urls for organiser

from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.index, name="h_index"),
    path("announcement/", views.announcement, name="h_announcement"),
    path("sponsor/", views.sponsor, name="h_sponsor"),
    path("doubt/", views.doubt, name="h_doubt"),
    
]