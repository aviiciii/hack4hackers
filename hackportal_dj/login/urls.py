# urls for organiser    

from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("land/", views.land, name="land"),
    path("logout/", views.logout_view, name="logout"),
]