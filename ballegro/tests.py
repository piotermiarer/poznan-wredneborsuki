from django.test import TestCase
from django.core.urlresolvers import resolve
from ballegro.models import Team, League, Clothes


class BasicViewTest:

    def test_url_resolves_to_correct_view(self):
        resolver_match = resolve(self.url)
        self.assertEqual(resolver_match.view_name, self.expected_view_name)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, self.expected_template)
        self.assertEqual(response.status_code, 200)

    def test_template_extends_after_base(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'ballegro/base.html')


class RootViewTest(TestCase, BasicViewTest):

    def setUp(self):
        self.url = '/'
        self.expected_view_name = 'ballegro:root'
        self.expected_template = 'ballegro/root.html'

    def test_teams_in_context(self):
        response = self.client.get(self.url)
        self.assertIn('teams', response.context)


class TeamShowViewTest(TestCase, BasicViewTest):

    def setUp(self):
        create_league_and_team()
        self.url = '/team_show/Lech Poznań'
        self.expected_view_name = 'ballegro:team_show'
        self.expected_template = 'ballegro/team_show.html'

    def test_team_in_context(self):
        response = self.client.get(self.url)
        self.assertIn('team', response.context)


class OffersViewTest(TestCase, BasicViewTest):

    def setUp(self):
        create_league_and_team()
        create_clothes()
        self.url = '/offers/Lech Poznań/hat'
        self.expected_view_name = 'ballegro:offers'
        self.expected_template = 'ballegro/offers.html'

    def test_team_and_results_in_context(self):
        response = self.client.get(self.url)
        self.assertIn('team', response.context)
        self.assertIn('results', response.context)


class AllTeamsViewTest(TestCase, BasicViewTest):

    def setUp(self):
        create_league_and_team()
        self.url = '/all_teams'
        self.expected_view_name = 'ballegro:all_teams'
        self.expected_template = 'ballegro/all_teams.html'

    def test_leagues_with_teams_in_context(self):
        response = self.client.get(self.url)
        self.assertIn('leagues_with_teams', response.context)


def create_clothes():
    hat = Clothes(name='czapka', category=None, add_team_to_phrase=True, url_name='hat')
    hat.save()


def create_league_and_team():
    new_league = League(name='Lotto Ekstraklasa')
    new_league.save()
    new_team = Team(name='Lech Poznań', image='lech_poznan.png', league=new_league)
    new_team.save()
