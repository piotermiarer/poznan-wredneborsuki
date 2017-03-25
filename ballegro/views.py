from django.shortcuts import get_object_or_404, render
from .models import Team

from urllib.parse import unquote

from .api_allegro import search_for
from .matches import get_upcoming

def root(request):
    teams = Team.objects.all()
    upcoming = get_upcoming()
    return render(request, 'ballegro/root.html',
        {'teams': teams, 'upcoming_matches': upcoming})

def team_show(request, team_name):
    team_name = team_name.replace('_', ' ')
    team = get_object_or_404(Team, name=team_name)
    return render(request, 'ballegro/team_show.html', {'team': team})

def search(request, clothes, team_name):
    team_name = team_name.replace('_', ' ')
    results = search_for(clothes, team_name)
    team = get_object_or_404(Team, name=team_name)
    return render(request, 'ballegro/search.html',
        {'team': team, 'results': results})
