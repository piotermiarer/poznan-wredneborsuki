from django.shortcuts import get_object_or_404, render
from urllib.parse import unquote

from .models import Team, League
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

def offers(request, team_name, clothes):
    results = get_offers(clothes, team_name)
    team = get_object_or_404(Team, name=team_name)
    return render(request, 'ballegro/offers.html',
        {'team': team, 'results': results})

def all_teams(request):
    leagues = League.objects.all()
    leagues_with_teams = {league: league.team_set.all() for league in leagues}
    return render(request, 'ballegro/all_teams.html', {'leagues_with_teams': leagues_with_teams})
