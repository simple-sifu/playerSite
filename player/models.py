import datetime
from django.db import models
from django.utils import timezone

class Player(models.Model):
    # Todo:
    # Some of the Integer/Date Fields are empty strings. 
    # Requirements dont specify substitute values for empty values, so
    # temporarily define everything has charField.

    playerID=models.CharField("Player ID", primary_key=True, db_index=True, max_length=20)
    birthYear=models.CharField(max_length=15, null=True, blank=True )
    birthMonth=models.CharField(max_length=15, null=True, blank=True )
    birthDay=models.CharField(max_length=15, null=True, blank=True )
    birthCountry=models.CharField(max_length=50)
    birthState=models.CharField(max_length=50)
    birthCity=models.CharField(max_length=50)
    deathYear=models.CharField(max_length=10)
    deathMonth=models.CharField(max_length=10)
    deathDay=models.CharField(max_length=10)
    deathCountry=models.CharField(max_length=50, null=True, blank=True )
    deathState=models.CharField(max_length=50, null=True, blank=True )
    deathCity=models.CharField(max_length=50, null=True, blank=True )
    nameFirst=models.CharField(max_length=50, null=True, blank=True )
    nameLast=models.CharField(max_length=50, null=True, blank=True )
    nameGiven=models.CharField(max_length=50, null=True, blank=True )
    weight=models.CharField(max_length=15, null=True, blank=True )
    height=models.CharField(max_length=15, null=True, blank=True )
    bats=models.CharField(max_length=2)
    throws=models.CharField(max_length=2)
    debut=models.CharField(max_length=15, null=True, blank=True )
    finalGame=models.CharField(max_length=15, null=True, blank=True )
    retroID=models.CharField(max_length=15, null=True, blank=True )
    bbrefID=models.CharField(max_length=15, null=True, blank=True )
    
    def __str__(self):
        return self.playerID
