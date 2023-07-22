from django.db import models

# Create 
class Hacker(models.Model):
    team_name = models.CharField(max_length=100, null=True, blank=True)
    lead_name = models.CharField(max_length=100, null=True, blank=True)
    lead_email = models.EmailField(null=True, blank=True)
    member1_name = models.CharField(max_length=100, null=True, blank=True)
    member2_name = models.CharField(max_length=100, null=True, blank=True)
    member3_name = models.CharField(max_length=100, null=True, blank=True)
    member4_name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Organiser(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    def _str_(self):
        return self.name