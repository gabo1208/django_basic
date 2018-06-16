import datetime

from django.db import models
from model_utils.models import TimeStampedModel
from apps.users.models import InterestTag, Profile
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')
    image = models.ImageField(null=True, blank=True)
    history = models.CharField(max_length=150, default='')
    tags = models.ManyToManyField(InterestTag, related_name='team_tag', blank=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    home_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='home_team', blank=True, null=True)
    away_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='away_team', blank=True, null=True)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE)
    score_set = models.BooleanField(default=False)
    score_home = models.CharField(default='0', max_length=5)
    score_away = models.CharField(default='0', max_length=5)
    match_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return (
            str(self.home_team) + ' - ' + str(self.away_team) + ' ' + str(self.match_datetime) +
            ' - ' + str(self.tournament)
        )

    def get_winner(self):
        if self.score_set:
            if self.score_home > self.score_away:
                return self.home_team
            elif self.score_home < self.score_away:
                return self.away_team
        return None

    def get_loser(self):
        if self.score_set:
            if self.score_home > self.score_away:
                return self.away_team
            elif self.score_home < self.score_away:
                return self.home_team
        return None


class GameResult(TimeStampedModel):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    score_home = models.CharField(default='0', max_length=5)
    score_away = models.CharField(default='0', max_length=5)

    def get_winner(self):
        if self.score_set:
            if self.score_home > self.score_away:
                return self.home_team
            elif self.score_home < self.score_away:
                return self.away_team
        return None

    def get_loser(self):
        if self.score_set:
            if self.score_home > self.score_away:
                return self.away_team
            elif self.score_home < self.score_away:
                return self.home_team
        return None

    def __str__(self):
        return(
            str(self.game.home_team) + ' ' + str(self.score_home) + ' - ' + str(self.score_away) + ' ' +
            str(self.game.away_team) + ' ' + self.user.user.email
        )


class GroupTeam(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    games_checked = models.IntegerField(default=0)

    class Meta:
        unique_together = ('team', 'group')

    def __str__(self):
        return str(self.group) + ' - ' + str(self.team) + ' - ' + str(self.score)

    def get_score(self):
        if self.games_checked < 3:
            self.games_checked = 0
            score = 0
            games_home = Game.objects.filter(
                tournament=self.group.tournament,
                home_team=self.team,
                match_datetime__lte=datetime.datetime(2018, 6, 29),
                score_set=True
            )
            games_away = games = Game.objects.filter(
                tournament=self.group.tournament,
                away_team=self.team,
                match_datetime__lte=datetime.datetime(2018, 6, 29),
                score_set=True
            )

            for game in games_home:
                self.games_checked += 1
                if game.score_home > game.score_away:
                    score += 3
                elif game.score_home == game.score_away:
                    score += 1

            for game in games_away:
                self.games_checked += 1
                if game.score_home < game.score_away:
                    score += 3
                elif game.score_home == game.score_away:
                    score += 1

            self.score = score
            self.save()

        return self.score


class Group(models.Model):
    name = models.CharField(max_length=50)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE)
    teams = models.ManyToManyField(
        'Team',
        through='GroupTeam',
        related_name='group_teams'
    )

    class Meta:
        unique_together = ('name', 'tournament')

    def __str__(self):
        return 'Group ' + self.name + ' - ' + str(self.tournament)

    def get_teams(self):
        return GroupTeam.objects.filter(group=self).order_by('-score')


class Tournament(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=150, unique=True)
    start_in = models.DateField(null=True, blank=True)
    ends_in = models.DateField(null=True, blank=True)
    # Real Results Fixture
    fixture = models.ManyToManyField('Game', related_name='fixture_games', blank=True)
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
    quiniela = models.ForeignKey('Quiniela', on_delete=models.CASCADE)
    results = models.ManyToManyField('GameResult', related_name='member_fixture_game_results')
    games_checked = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

    class Meta:
        unique_together=(('user', 'tournament', 'quiniela'),)

    def __str__(self):
        return self.user.user.username + '(' + self.user.user.email + ') - ' + self.tournament.name + ' - ' + self.quiniela.name

    def get_score(self, score_type):
        flag = False

        for result in (self.results.filter(game__match_datetime__lte=datetime.datetime.today()+ datetime.timedelta(hours=2)).
                order_by('game__match_datetime')[self.games_checked:]):

            flag = True
            # If the Game hasan official result, calculate the score and cache the instance
            if result.game.score_set:
                # 3 points for the game result
                if score_type == Quiniela.TOTAL_SCORE:
                    if(result.score_home == result.game.score_home and 
                        result.score_away == result.game.score_away):
                        self.score += 3
                # 1 point for equal score, 1 point for game result
                else:
                    if result.score_home == result.game.score_home:
                        self.score += 1

                    if result.score_away == result.game.score_away:
                        self.score += 1

                    if((result.score_away < result.score_home and
                        result.game.score_away < result.game.score_home) or
                        (result.score_away == result.score_home and
                        result.game.score_away == result.game.score_home) or
                        (result.score_away > result.score_home and
                        result.game.score_away > result.game.score_home)):
                        self.score += 1

                self.games_checked += 1
            else:
                break

        if flag:
            self.save()

        return self.score


class Quiniela(TimeStampedModel):
    TOTAL_SCORE = 'TO'
    EACH_SCORE = 'EA'
    TOTAL_PREDICTION_QUINIELA = 'TQ'
    PHASES_QUINIELA = 'PQ'

    TOURNAMENT_SCORE_CHOICES = (
        (TOTAL_SCORE, 'Game Result Points.'),
        (EACH_SCORE, 'Game Result and Teams Score Points.'),
    )
    QUINIELA_TYPE_CHOICES = (
        (TOTAL_PREDICTION_QUINIELA, 'Predict all games and scores.'),
        (PHASES_QUINIELA, 'Predict just current phase games and scores.'),
    )

    admin = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=150, default='')
    members = models.ManyToManyField(Profile, related_name='quiniela_members')
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE, blank=True, null=True)
    public = models.BooleanField(default=False)
    score_type = models.CharField(
        max_length=2,
        choices=TOURNAMENT_SCORE_CHOICES,
        default=TOTAL_SCORE
    )
    score_type_cache = models.CharField(
        max_length=2,
        choices=TOURNAMENT_SCORE_CHOICES,
        default=TOTAL_SCORE,
        editable=False
    )
    quiniela_type = models.CharField(
        max_length=2,
        choices=QUINIELA_TYPE_CHOICES,
        default=EACH_SCORE
    )
    quiniela_type_cache = models.CharField(
        max_length=2,
        choices=QUINIELA_TYPE_CHOICES,
        default=EACH_SCORE,
        editable=False
    )
    tags = models.ManyToManyField(InterestTag, related_name='quiniela_tag', blank=True)

    class Meta:
        unique_together = ('admin', 'name', 'tournament')

    def __init__(self, *args, **kwargs):
        super(Quiniela, self).__init__(*args, **kwargs)
        self.score_type_cache = self.score_type
        self.quiniela_type_cache = self.quiniela_type

    def __str__(self):
        return self.name + ' - ' + str(self.tournament) + ' - owner: ' + self.admin.user.username


class OscarCoin(TimeStampedModel):
    value = models.IntegerField(default=0)


##################### SIGNALS ########################
@receiver(pre_save, sender=Quiniela)
def save_quiniela(sender, instance, **kwargs):
    if instance.score_type != instance.score_type_cache or instance.quiniela_type != instance.quiniela_type_cache:
        for memberfixture in MemberFixture.objects.filter(tournament=instance.tournament):
            memberfixture.score = 0
            memberfixture.games_checked = 0
            memberfixture.save()

        instance.score_type_cache = instance.score_type
