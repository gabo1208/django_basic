from django.db import models
from model_utils.models import TimeStampedModel
from apps.users.models import InterestTag, Profile

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(null=True, blank=True)
    history = models.CharField(max_length=150, default='')
    tags = models.ManyToManyField(InterestTag, related_name="team_tag", blank=True)

class Game(models.Model):
	home_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name="home_team")
	away_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name="away_team")
	score_home = models.CharField(max_length=3, default='0')
	score_away = models.CharField(max_length=3, default='0')
	limit_date = models.DateField(null=True, blank=True)
	match_date = models.DateField(null=True, blank=True)

class Tournament(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=150, unique=True)
    start_in = models.DateField(null=True, blank=True)
    ends_in = models.DateField(null=True, blank=True)
    fixture = models.ManyToManyField('Game', related_name="fixture_games")
    tags = models.ManyToManyField(InterestTag, related_name="tournament_tag", blank=True)

class Quiniela(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=150, default='')
    members = models.ManyToManyField(Profile, related_name="quiniela_members")
    tournaments = models.ManyToManyField('Tournament', related_name="quiniela_tournamets")
    tags = models.ManyToManyField(InterestTag, related_name="quiniela_tag", blank=True)