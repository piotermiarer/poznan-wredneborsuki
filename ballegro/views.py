from django.shortcuts import get_object_or_404, render
from .models import Team

from urllib.parse import unquote

def root(request):
    teams = Team.objects.all()
    return render(request, 'ballegro/root.html', {'teams': teams})

def team_show(request, team_name):
    team_name = team_name.replace('_', ' ')
    team = get_object_or_404(Team, name=team_name)
    return render(request, 'ballegro/team_show.html', {'team': team})
