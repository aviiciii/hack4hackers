from django.db import models

# Create 
class Hacker(models.Model):
    team_name = models.CharField(max_length=100)
    lead_name = models.CharField(max_length=100)
    lead_email = models.EmailField()
    member1_name = models.CharField(max_length=100)
    member2_name = models.CharField(max_length=100)
    member3_name = models.CharField(max_length=100)
    member4_name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Organizer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
    # Add other fields as needed, such as organization, role, etc.

    def _str_(self):
        return self.name