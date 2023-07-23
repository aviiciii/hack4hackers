from django.db import models

# Create your models here.

class Doubt(models.Model):
    id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=100)
    doubt = models.CharField(max_length=1000)
    recipient = models.CharField(max_length=100)
    answer = models.TextField(default="", blank=True, null=True)

    def __str__(self):
        return self.team_name
