from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db.models import F

from league.models import Match, Season


# Create your views here.
def default_view(request):
    return HttpResponse("Default page")


def display_all_matches(request, season_name):
    season = Season.objects.all().filter(season_name=season_name).values_list('pk')[0]
    matches = Match.objects.all().filter(season=season)
    context = {'season': season_name, 'matches': matches}
    return render(request, 'league/display_all_matches.html', context=context)


def display_match_details(request, season_name, match_id):
    season = Season.objects.all().filter(season_name=season_name).values_list('pk')[0]
    match = Match.objects.all().filter(season=season, match_no=match_id)
    context = {'match': match}
    return render(request, 'league/match_details.html', context=context)


def display_matches_team(request, team, location):
    if location == 'all':
        matches_home = Match.objects.all().filter(home_team=team)
        matches_away = Match.objects.all().filter(away_team=team)
        matches = matches_home | matches_away
        location = 'All'
    elif location == 'home':
        matches = Match.objects.all().filter(home_team=team)
        location = 'Home'
    elif location == 'away':
        matches = Match.objects.all().filter(away_team=team)
        location = 'Away'
    matches = matches.order_by('season', 'match_no')
    context = {'home': location, 'team': team, 'matches': matches}
    return render(request, 'league/display_matches_team.html', context=context)


def display_matches_team_result(request, team, result, location):
    if result == 'win':
        if location == 'all':
            matches_home = Match.objects.all().filter(home_team=team, result='H')
            matches_away = Match.objects.all().filter(away_team=team, result='A')
            matches = matches_home | matches_away
            location = 'All'
        elif location == 'home':
            matches = Match.objects.all().filter(home_team=team, result='H')
            location = 'Home'
        elif location == 'away':
            matches = Match.objects.all().filter(away_team=team, result='A')
            location = 'Away'
    elif result == 'loss':
        if location == 'all':
            matches_home = Match.objects.all().filter(home_team=team, result='A')
            matches_away = Match.objects.all().filter(away_team=team, result='H')
            matches = matches_home | matches_away
            location = 'All'
        elif location == 'home':
            matches = Match.objects.all().filter(home_team=team, result='A')
            location = 'Home'
        elif location == 'away':
            matches = Match.objects.all().filter(away_team=team, result='H')
            location = 'Away'
    elif result == 'draw':
        if location == 'all':
            matches_home = Match.objects.all().filter(home_team=team, result='D')
            matches_away = Match.objects.all().filter(away_team=team, result='D')
            matches = matches_home | matches_away
            location = 'All'
        elif location == 'home':
            matches = Match.objects.all().filter(home_team=team, result='D')
            location = 'Home'
        elif location == 'away':
            matches = Match.objects.all().filter(away_team=team, result='D')
            location = 'Away'
    else:
        return Http404()
    matches = matches.order_by('season', 'match_no')
    context = {'home': location, 'team': team, 'matches': matches}
    return render(request, 'league/display_matches_team.html', context=context)


def display_matches_bw_teams(request, team1, team2):
    matches_1 = Match.objects.all().filter(home_team=team1, away_team=team2)
    matches_2 = Match.objects.all().filter(home_team=team2, away_team=team1)
    matches = matches_1 | matches_2
    matches = matches.order_by('season', 'match_no')
    context = {'team1': team1, 'team2': team2, 'matches': matches}
    return render(request, 'league/matches_bw_teams.html', context=context)


def comebacks(request, season_name, team, location):
    comebacks_home = Match.objects.all().filter(result='H').filter(home_team_ht_goals__lt=F('away_team_ht_goals'))
    comebacks_away = Match.objects.all().filter(result='A').filter(away_team_ht_goals__lt=F('home_team_ht_goals'))
    comebacks = comebacks_home | comebacks_away
    comebacks = comebacks.order_by('season', 'match_no')
    if season_name != 'all':
        season = Season.objects.all().filter(season_name=season_name).values_list('pk')[0]
        comebacks = comebacks.filter(season=season)
    if team != 'all':
        comebacks_home = comebacks.filter(home_team=team).filter(result='H')
        comebacks_away = comebacks.filter(away_team=team).filter(result='A')
        comebacks = comebacks_home | comebacks_away
    if location == 'home':
        comebacks = comebacks.filter(result='H')
    elif location == 'away':
        comebacks = comebacks.filter(result='A')
    context = {'matches': comebacks}
    return render(request, 'league/comebacks.html', context=context)

