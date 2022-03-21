import datetime
from django.db import models
from django.utils import timezone

class Player(models.Model):
    player_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.player_text

