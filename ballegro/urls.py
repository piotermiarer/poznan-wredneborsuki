from django.conf.urls import url
from . import views

app_name='ballegro'
urlpatterns = [
    url(r'^$', views.root, name='root'),
]
