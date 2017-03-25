from django.db import models


class League(models.Model):

    name = models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):

    name = models.TextField()
    image = models.TextField()
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
