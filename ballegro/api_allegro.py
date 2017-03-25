import requests


def get_offers(clothes, team_name, category=None):
    search_phrase = clothes + ' ' + team_name
    parameters = {'phrase': search_phrase, 'country.code': 'PL'}
    if category is not None:
        parameters['category.name'] = category
    response = requests.get(
        'https://allegroapi.io/offers',
        params=parameters,
        headers={
            'Api-Key': 'eyJjbGllbnRJZCI6ImE0MWY1YjJhLThlODctNGI4Yi1iNmZlLTc0Y2M3NjM3MjBkNyJ9.ogVV_a9RUOMa1OWFZOTmgTkdk-U37vTliDCBUQ1YySU=',
            'User-Agent': 'hackaton2017 (Client-Id 656cbe47-b17d-46c2-bae1-3222c8777d5b) Platform',
            'Accept': 'application/vnd.allegro.public.v1+json'
        }
    )
    return response.json()['offers']
