import json
import sys
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()
from ballegro.models import Team


with open('leagues.json', 'r', encoding="utf8") as f:
    leagues = json.load(f)

for league in leagues:
    if league['name'] == sys.argv[1]:
        for team in league['teams']:
            new_team = Team(name=team['name'], image=team['crest_url'])
            new_team.save()
