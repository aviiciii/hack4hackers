# urls for organiser

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="o_index"),
    path("hackthon/", views.hackathon_details, name="o_hackathon_details"),
]