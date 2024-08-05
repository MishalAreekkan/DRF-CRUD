from django.db import models

# Create your models here.

class Team(models.Model):
    teamName = models.CharField(max_length=50)
    
class PersonDetails(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='member',null=True,blank=True)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=500)
    domain = models.CharField(max_length=500)

    
class Demo(models.Model):
    name = models.CharField(max_length=100)
    palce = models.CharField(max_length=100)
    number = models.IntegerField()