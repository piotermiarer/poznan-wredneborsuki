from django.conf.urls import url
from . import views

app_name='ballegro'
urlpatterns = [
    url(r'^$', views.root, name='root'),
    url(r'^team_show/(?P<team_name>.+)', #a-zA-Z0-9%-_
        views.team_show, name='team_show'),
]
