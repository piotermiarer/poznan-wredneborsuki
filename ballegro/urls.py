from django.conf.urls import url
from . import views


app_name='ballegro'
urlpatterns = [
    url(r'^$', views.root, name='root'),
    url(r'^team_show/(?P<team_name>.+)',
        views.team_show, name='team_show'),
    url(r'^offers/(?P<team_name>.+)/(?P<clothes>.+)',
        views.offers, name='offers'),
    url(r'^all_teams$', views.all_teams, name='all_teams'),
]
