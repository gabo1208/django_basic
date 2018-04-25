from django.db import models
from model_utils.models import TimeStampedModel
from apps.users.models import InterestTag, Profile

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')
    image = models.ImageField(null=True, blank=True)
    history = models.CharField(max_length=150, default='')
    tags = models.ManyToManyField(InterestTag, related_name='team_tag', blank=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    home_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='away_team')
    score_home = models.IntegerField(default=0)
    score_away = models.IntegerField(default=0)
    context = models.ManyToManyField(
        'Tournament',
        through='GameContext',
        related_name='game_context'
    )
    limit_date = models.DateField(null=True, blank=True)
    match_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.home_team) + ' - ' + str(self.away_team) + ' ' + str(self.match_date)

class GameResult(TimeStampedModel):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    score_home = models.IntegerField(default=0)
    score_away = models.IntegerField(default=0)

class GameContext(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE)
    context = models.CharField(max_length=50, default='Group A/8ths/Semifinals')

    class Meta:
        unique_together=(('tournament', 'context'),)

class Tournament(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=150, unique=True)
    start_in = models.DateField(null=True, blank=True)
    ends_in = models.DateField(null=True, blank=True)

    # Real Results Fixture
    fixture = models.ManyToManyField('Game', related_name='fixture_games')
    # Fixtures from each members
    members_results = models.ManyToManyField(
        Profile,
        through='MemberFixture',
        related_name='members_fixture_games'
    )

    tags = models.ManyToManyField(InterestTag, related_name='tournament_tag', blank=True)

    def __str__(self):
        return self.name

class MemberFixture(TimeStampedModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE)
    results = models.ManyToManyField('GameResult', related_name='member_fixture_game_results')
    score = models.IntegerField(default=0)

    class Meta:
        unique_together=(('user', 'tournament'),)

class Quiniela(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=150, default='')
    members = models.ManyToManyField(Profile, related_name='quiniela_members')
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(InterestTag, related_name='quiniela_tag', blank=True)

    def __str__(self):
        return self.name