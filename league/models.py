from django.db import models


class Season(models.Model):
    # Season name to be in format YYYY-YY (Ex: 2019-20)
    season_name = models.CharField(max_length=7)

    def __str__(self):
        return self.season_name


class Match(models.Model):

    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    match_no = models.IntegerField(default=0)
    home_team = models.CharField(max_length=30)
    away_team = models.CharField(max_length=30)
    referee = models.CharField(max_length=30)
    home_team_ht_goals = models.IntegerField(default=0)
    away_team_ht_goals = models.IntegerField(default=0)
    home_team_ft_goals = models.IntegerField(default=0)
    away_team_ft_goals = models.IntegerField(default=0)
    home_team_shots = models.IntegerField(default=0)
    away_team_shots = models.IntegerField(default=0)
    home_team_shots_on_target = models.IntegerField(default=0)
    away_team_shots_on_target = models.IntegerField(default=0)
    result = models.CharField(max_length=1)  # 'H'/'A'/'D'

    def __str__(self):
        return f"{self.season} - {self.match_no} - {self.home_team} v {self.away_team}"
