# urls for organiser

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="o_index"),
    
]