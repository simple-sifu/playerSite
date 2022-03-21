from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.Serializer):

    playerID=serializers.CharField(max_length=40, allow_blank=True)
    birthYear=serializers.CharField(max_length=10, allow_blank=True)
    birthMonth=serializers.CharField(max_length=10, allow_blank=True)
    birthDay=serializers.CharField(max_length=10, allow_blank=True)
    birthCountry=serializers.CharField(max_length=20, allow_blank=True)
    birthState=serializers.CharField(max_length=4, allow_blank=True)
    birthCity=serializers.CharField(max_length=10, allow_blank=True)
    deathYear=serializers.CharField(max_length=10, allow_blank=True)
    deathMonth=serializers.CharField(max_length=10, allow_blank=True)
    deathDay=serializers.CharField(max_length=10, allow_blank=True)
    deathCountry=serializers.CharField(max_length=50, allow_blank=True )
    deathState=serializers.CharField(max_length=50, allow_blank=True )
    deathCity=serializers.CharField(max_length=50, allow_blank=True )
    nameFirst=serializers.CharField(max_length=50, allow_blank=True )
    nameLast=serializers.CharField(max_length=50, allow_blank=True )
    nameGiven=serializers.CharField(max_length=50, allow_blank=True )
    weight=serializers.CharField(max_length=15, allow_blank=True )
    height=serializers.CharField(max_length=15, allow_blank=True )
    bats=serializers.CharField(max_length=2, allow_blank=True)
    throws=serializers.CharField(max_length=2, allow_blank=True)
    debut=serializers.CharField(max_length=15, allow_blank=True )
    finalGame=serializers.CharField(max_length=15, allow_blank=True )
    retroID=serializers.CharField(max_length=15, allow_blank=True )
    bbrefID=serializers.CharField(max_length=15, allow_blank=True )
