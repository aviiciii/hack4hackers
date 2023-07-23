from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Hackathon)
admin.site.register(models.Sponsor)

admin.site.register(models.Announcement)
