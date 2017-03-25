import requests

def search_for(clothes, team_name):

    r2 = requests.get(
        'https://allegroapi.io/offers',
        params={'phrase': clothes + ' ' + team_name, 'country.code': 'PL'},
        headers={'Api-Key': 'eyJjbGllbnRJZCI6ImE0MWY1YjJhLThlODctNGI4Yi1iNmZlLTc0Y2M3NjM3MjBkNyJ9.ogVV_a9RUOMa1OWFZOTmgTkdk-U37vTliDCBUQ1YySU=',
            'User-Agent': 'hackaton2017 (Client-Id 656cbe47-b17d-46c2-bae1-3222c8777d5b) Platform',
            'Accept': 'application/vnd.allegro.public.v1+json'}
    )

    return r2.json()['offers']
