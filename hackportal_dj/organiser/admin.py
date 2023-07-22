from django.contrib import admin

# Register your models here.

from .models import Hackathon, Sponsor

admin.site.register(Hackathon)
admin.site.register(Sponsor)
