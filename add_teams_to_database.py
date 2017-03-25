import json
import sys
import os
import requests
from urllib.parse import unquote
from PIL import Image

# do some django magic to be able to modify database
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

from ballegro.models import Team, League


def main():
    """
    Adding leagues and teams to database.
    It includes downloading images and resizing them.
    """
    with open('leagues.json', 'r', encoding="utf8") as f:
        leagues = json.load(f)

    distinct_leagues = {"1. Bundesliga 2016/17", "Premier League 2016/17",
        "Serie A 2016/17", "Primera Division 2016/17", "Ligue 1 2016/17",
        "Eredivisie 2016/17","Primeira Liga 2016/17"}

    add_all_leagues = False
    if len(sys.argv) < 2:
        add_all_leagues = True

    for league in leagues:
        if (add_all_leagues and league['name'] in distinct_leagues) or (not add_all_leagues and league['name'] == sys.argv[1]):
            new_league = League(name=league['name'])
            new_league.save()
            for team in league['teams']:
                url = team['crest_url']
                response = requests.get(url)
                filename = url.split('/')[-1]
                image_filename = 'static/images/' + unquote(filename)
                with open('ballegro/' + image_filename, 'wb') as f:
                    f.write(response.content)
                if not image_filename.endswith('.svg'):
                    resize_photo('ballegro/' + image_filename)
                new_team = Team(name=team['name'], image=image_filename, league=new_league)
                new_team.save()


def resize_photo(path):
    productImage = Image.open(path)
    width, height = productImage.size
    photoNeedsChange = False
    MAX_SIZE = 200
    if width > height and width > MAX_SIZE:
        proportion = width / MAX_SIZE
        productImage = productImage.resize((MAX_SIZE, int(height / proportion)), Image.ANTIALIAS)
        photoNeedsChange = True
    elif height >= width and height > MAX_SIZE:
        proportion = height / MAX_SIZE
        productImage = productImage.resize((int(width / proportion), MAX_SIZE), Image.ANTIALIAS)
        photoNeedsChange = True
    if photoNeedsChange:
        productImage.save(path, quality=90)


if __name__ == '__main__':
    main()
