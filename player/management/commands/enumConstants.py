from enum import IntEnum


# 0 - playerID
# 1 - birthYear
# 2 - birthMonth
# 3 - birthDay
# 4 - birthCountry
# 5 - birthState
# 6 - birthCity
# 7 - deathYear
# 8 - deathMonth
# 9 - deathDay
# 10 - deathCountry
# 11 - deathState
# 12 - deathCity
# 13 - nameFirst
# 14 - nameLast
# 15 - nameGiven
# 16 - weight
# 17 - height
# 18 - bats
# 19 - throws
# 20 - debut
# 21 - finalGame
# 22 - retroID
# 23 - bbrefID

class PlayerColumns(IntEnum):
    PLAYER_ID = 0
    BIRTH_YEAR = 1
    BIRTH_MONTH = 2
    BIRTH_DAY = 3
    BIRTH_COUNTRY = 4
    BIRTH_STATE = 5
    BIRTH_CITY = 6
    DEATH_YEAR = 7
    DEATH_MONTH = 8
    DEATH_DAY = 9
    DEATH_COUNTRY = 10
    DEATH_STATE = 11
    DEATH_CITY = 12
    NAME_FIRST = 13
    NAME_LAST = 14
    NAME_GIVEN = 15
    WEIGHT = 16
    HEIGHT = 17
    BATS = 18
    THROWS = 19
    DEBUT = 20
    FINAL_GAME = 21
    RETRO_ID = 22
    BBREF_ID = 23
