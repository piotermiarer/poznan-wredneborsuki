from django.test import TestCase
from django.core.urlresolvers import resolve
from ballegro.models import Team


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
        self.url = '/'
        self.expected_view_name = 'ballegro:team_show'
        self.expected_template = 'ballegro/team_show.html'

    def test_teams_in_context(self):
        response = self.client.get(self.url)
        self.assertIn('team', response.context)
