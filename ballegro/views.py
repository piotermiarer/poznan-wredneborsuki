from django.shortcuts import get_object_or_404, render
from urllib.parse import unquote
import json
from django.http import HttpResponse

from .models import Team, League, Clothes
from .api_allegro import get_offers
from .matches import get_upcoming

def root(request):
    all_teams = Team.objects.all()
    upcoming, upcoming_teams = get_upcoming()
    teams = []
    for team in all_teams:
        if team.name in upcoming_teams[:10]:
            teams.append(team)

    return render(request, 'ballegro/root.html',
        {'teams': teams, 'upcoming_matches': upcoming})

def team_show(request, team_name):
    team = get_object_or_404(Team, name=team_name)
    return render(request, 'ballegro/team_show.html', {'team': team})


def offers(request, team_name, clothes):
    team = get_object_or_404(Team, name=team_name)
    clothes_object = get_object_or_404(Clothes, url_name=clothes)
    clothes_phrase = clothes_object.name
    team_phrase = ''

    if (clothes_object.add_team_to_phrase):
        team_phrase = team_name
    results = get_offers(clothes_phrase, team_phrase,
        clothes_object.category)

    if clothes == 'ball':
        league_name = team.league.name
        clothes_phrase += ' ' + league_name
        team_phrase = ''
        results += get_offers(clothes_phrase, team_phrase,
            clothes_object.category)

    return render(request, 'ballegro/offers.html',
        {'team': team, 'results': results})

def all_teams(request):
    leagues = League.objects.all()
    leagues_with_teams = {league: league.team_set.all() for league in leagues}
    return render(request, 'ballegro/all_teams.html', {'leagues_with_teams': leagues_with_teams})

def search_team(request, team_name):
    teams = Team.objects.filter(name__contains=team_name)
    team_names = teams.values_list('name')
    image_names = teams.values_list('url_name')
    result = []
    for team in zip(team_names, image_names):
        result.append(team)
    return HttpResponse(json.dumps(result), content_type='application/json')
