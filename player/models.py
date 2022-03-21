import datetime
from django.db import models
from django.utils import timezone

class Player(models.Model):
    playerID=models.CharField("Player ID", primary_key=True, db_index=True, max_length=20)
    birthYear=models.IntegerField()
    birthMonth=models.IntegerField()
    birthDay=models.IntegerField()
    birthCountry=models.CharField(max_length=50)
    birthState=models.CharField(max_length=50)
    birthCity=models.CharField(max_length=50)
    deathYear=models.CharField(max_length=10)
    deathMonth=models.CharField(max_length=10)
    deathDay=models.CharField(max_length=10)
    deathCountry=models.CharField(max_length=50)
    deathState=models.CharField(max_length=50)
    deathCity=models.CharField(max_length=50)
    nameFirst=models.CharField(max_length=50)
    nameLast=models.CharField(max_length=50)
    nameGiven=models.CharField(max_length=50)
    weight=models.IntegerField()
    height=models.IntegerField()
    bats=models.CharField(max_length=2)
    throws=models.CharField(max_length=2)
    debut=models.CharField(max_length=10)
    finalGame=models.CharField(max_length=10)
    retroID=models.CharField(max_length=10)
    bbrefID=models.CharField(max_length=10)
    
    def __str__(self):
        return self.nameLast
