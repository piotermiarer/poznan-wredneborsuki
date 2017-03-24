from django.shortcuts import render
from .models import Team


def root(request):
    teams = Team.objects.all()
    return render(request, 'ballegro/root.html', {'teams': teams})
