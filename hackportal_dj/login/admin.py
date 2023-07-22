from django.contrib import admin

# Register your models here.
from .models import Hacker, Organiser


admin.site.register(Hacker)
admin.site.register(Organiser)