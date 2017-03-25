import json
import sys
import os
import requests
from urllib.parse import unquote
from PIL import Image

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()
from ballegro.models import Team


def change_photo(path):
    productImage = Image.open(path)
    width, height = productImage.size
    photoNeedsChange = False
    if width > height and width > 200:
        proportion = width / 200
        productImage = productImage.resize((200, int(height / proportion)), Image.ANTIALIAS)
        photoNeedsChange = True
    elif height >= width and height > 200:
        proportion = height / 200
        productImage = productImage.resize((int(width / proportion), 200), Image.ANTIALIAS)
        photoNeedsChange = True
    if width == 200 and height == 200:
        photoNeedsChange = True
    if photoNeedsChange:
        productImage.save(path, quality=90)

with open('leagues.json', 'r', encoding="utf8") as f:
    leagues = json.load(f)

for league in leagues:
    if league['name'] == sys.argv[1]:
        for team in league['teams']:
            url = team['crest_url']
            response = requests.get(url)
            filename = url.split('/')[-1]
            image_filename = 'static/images/' + unquote(filename)
            with open('ballegro/' + image_filename, 'wb') as f:
                f.write(response.content)
            if not image_filename.endswith('.svg'):
                change_photo('ballegro/' + image_filename)
            new_team = Team(name=team['name'], image=image_filename)
            new_team.save()
