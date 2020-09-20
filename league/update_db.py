import pandas

from league.models import Season, Match

import os


DATA_ROOT = r'D:\Python\working\EPL Table'

path = os.path.join(DATA_ROOT, '2011-12.csv')
data = pandas.read_csv(path)


for i in range(len(data)):
    match_data = data.loc[i]
    season = '2011-12'
    match_no = i+1
    home_team = match_data['HomeTeam']
    away_team = match_data['AwayTeam']
    referee = match_data['Referee']
    home_team_ht_goals = match_data['HTHG']
    away_team_ht_goals = match_data['HTAG']
    home_team_ft_goals = match_data['FTHG']
    away_team_ft_goals = match_data['FTAG']
    home_team_shots = match_data['HS']
    away_team_shots = match_data['AS']
    home_team_shots_on_target = match_data['HST']
    away_team_shots_on_target = match_data['AST']
    result = match_data['FTR']

    Match.objects.create(
        season=season_2011_12,
        match_no=i+1,
        home_team=home_team,
        away_team=away_team,
        referee=referee,
        home_team_ht_goals=home_team_ht_goals,
        away_team_ht_goals=away_team_ht_goals,
        home_team_ft_goals=home_team_ft_goals,
        away_team_ft_goals=away_team_ft_goals,
        home_team_shots=home_team_shots,
        away_team_shots=away_team_shots,
        home_team_shots_on_target=home_team_shots_on_target,
        away_team_shots_on_target=away_team_shots_on_target,
        result=result
    )

