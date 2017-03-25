import requests, re


def get_offers(clothes, team_phrase, category=None):
    search_phrase = clothes + ' ' + team_phrase
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
    offers = response.json()['offers']

    final_offers = []
    for offer in offers:
        name = offer['name']
        if re.search(clothes.split(' ')[0] + '\\b', offer['name'], re.IGNORECASE):
            if team_phrase != '' and not re.search(team_phrase, offer['name'], re.IGNORECASE):
                continue
            else:
                final_offers.append(offer)
    return final_offers
