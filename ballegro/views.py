from django.shortcuts import get_object_or_404, render
from urllib.parse import unquote

from .models import Team, League, Clothes
from .api_allegro import get_offers
from .matches import get_upcoming

def root(request):
    teams = Team.objects.all()
    upcoming = get_upcoming()
    return render(request, 'ballegro/root.html',
        {'teams': teams, 'upcoming_matches': upcoming})

def team_show(request, team_name):
    team = get_object_or_404(Team, name=team_name)
    return render(request, 'ballegro/team_show.html', {'team': team})


def offers(request, team_name, clothes, page):
    OFFERS_PER_PAGE = 12
    first_index = (int(page) - 1) * OFFERS_PER_PAGE
    team = get_object_or_404(Team, name=team_name)
    clothes_object = get_object_or_404(Clothes, url_name=clothes)
    clothes_phrase = clothes_object.name
    if clothes == 'piłka':
        league_name = team.league.name
        clothes_phrase += ' ' + league_name
    team = get_object_or_404(Team, name=team_name)
    results = get_offers(clothes_phrase, team_name, clothes_object.category)[first_index:first_index + OFFERS_PER_PAGE]
    return render(request, 'ballegro/offers.html',
        {'team': team, 'results': results, 'page': page})

def all_teams(request):
    leagues = League.objects.all()
    leagues_with_teams = {league: league.team_set.all() for league in leagues}
    return render(request, 'ballegro/all_teams.html', {'leagues_with_teams': leagues_with_teams})
