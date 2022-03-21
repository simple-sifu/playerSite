from django.core.management.base import BaseCommand, CommandError
from player.models import Player
from django.db import IntegrityError
from .enumConstants import PlayerColumns

import csv


class Command(BaseCommand):
    help = 'Load Player csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--filename', type=str)

    def handle(self, *args, **kwargs):

        if Player.objects.all().count() > 0:
            val = input("The tables already has records loaded !!! Are you sure you want to load CSV File ?(y/n):") 
            if val.upper() != 'Y':
                self.stdout.write("cvs upload successfully aborted !!")
                return

        csvfile = './data/' + kwargs['filename']

        row_count = 0
        with open(csvfile, 'rt') as file:
            rows = csv.reader(file, delimiter=",", quotechar='"')
            for row in rows:
                
                if rows.line_num == 1:
                    continue
                try:
                    self.stdout.write("insert row with playerId: "+ row[PlayerColumns.PLAYER_ID])
                    # Todo:
                    # Some of the Integer/Date Fields are empty strings. 
                    # Requirements dont specify substitute values for empty values, so
                    # temporarily define everything has charField.
                    player, created = Player.objects.update_or_create(
                            playerID=row[PlayerColumns.PLAYER_ID],
                            birthYear=row[PlayerColumns.BIRTH_YEAR],
                            birthMonth=row[PlayerColumns.BIRTH_MONTH],
                            birthDay=row[PlayerColumns.BIRTH_DAY],
                            birthCountry=row[PlayerColumns.BIRTH_COUNTRY],
                            birthState=row[PlayerColumns.BIRTH_STATE],
                            birthCity=row[PlayerColumns.BIRTH_CITY],
                            deathYear=row[PlayerColumns.DEATH_YEAR],
                            deathMonth=row[PlayerColumns.DEATH_MONTH],
                            deathDay=row[PlayerColumns.DEATH_DAY],
                            deathCountry=row[PlayerColumns.DEATH_COUNTRY],
                            deathState=row[PlayerColumns.DEATH_STATE],
                            deathCity=row[PlayerColumns.DEATH_CITY],
                            nameFirst=row[PlayerColumns.NAME_FIRST],
                            nameLast=row[PlayerColumns.NAME_LAST],
                            nameGiven=row[PlayerColumns.NAME_GIVEN],
                            weight=row[PlayerColumns.WEIGHT],
                            height=row[PlayerColumns.HEIGHT],
                            bats=row[PlayerColumns.BATS],
                            throws=row[PlayerColumns.THROWS],
                            debut=row[PlayerColumns.DEBUT],
                            finalGame=row[PlayerColumns.FINAL_GAME],
                            retroID=row[PlayerColumns.RETRO_ID],
                            bbrefID=row[PlayerColumns.BBREF_ID],
                    )

                    row_count = rows.line_num
                except IntegrityError as e:
                    self.stdout.write("ErrorMessage1: "+str(e))
                    return

            self.stdout.write(" - Loaded " + str(row_count) + " rows into Player Table")
