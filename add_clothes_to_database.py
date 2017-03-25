import os

# do some django magic to be able to modify database
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

from ballegro.models import Team, League, Clothes


CLOTHES = {
    'shorts': {'category': 'Sport i Turystyka', 'name': 'spodenki', 'add_team_to_phrase': True},
    'socks': {'category': None, 'name': 'getry', 'add_team_to_phrase': True},
    'shirt': {'category': 'Klubowe', 'name': 'koszulka', 'add_team_to_phrase': True},
    'boots': {'category': 'Piłka nożna', 'name': 'korki', 'add_team_to_phrase': False},
    'ball': {'category': 'Piłki', 'name': 'piłka', 'add_team_to_phrase': True},
    'scarf': {'category': 'Sport i Turystyka', 'name': 'szalik', 'add_team_to_phrase': True},
    'hat': {'category': None, 'name': 'czapka', 'add_team_to_phrase': True},
    'tracksuit': {'category': 'Sporty drużynowe', 'name': 'spodenki', 'add_team_to_phrase': True},
    'hoodie': {'category': None, 'name': 'bluza', 'add_team_to_phrase': True}
}

def main():
    """
    Adding clothes to database.
    """
    for key, single_clothes in CLOTHES.items():
        if single_clothes['name']:
            new_clothes = Clothes(
                url_name=key,
                name=single_clothes['name'],
                category=single_clothes['category'],
                add_team_to_phrase=single_clothes['add_team_to_phrase']
            )
        else:
            new_clothes = Clothes(
                name=single_clothes['name'],
                add_team_to_phrase=single_clothes['add_team_to_phrase']
            )
        new_clothes.save()


if __name__ == '__main__':
    main()
