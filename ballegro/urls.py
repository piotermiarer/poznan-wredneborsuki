from django.conf.urls import url
from . import views

app_name='ballegro'
urlpatterns = [
    url(r'^$', views.root, name='root'),
    url(r'^team_show/(?P<team_name>.+)',
        views.team_show, name='team_show'),
    url(r'^search/(?P<clothes>.+)/(?P<team_name>.+)',
        views.search, name='search'),
    url(r'^index$', views.index, name='index'),
]
