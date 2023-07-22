from django.db import models

# Create your models here.

class Sponsor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    website = models.URLField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Hackathon(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=200, blank=True, null=True)
    theme = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    eligibility = models.CharField(max_length=200, blank=True, null=True)    
    team_size = models.CharField(max_length=20, blank=True, null=True)
    prizes = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name



