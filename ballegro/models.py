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


class Clothes(models.Model):

    name = models.TextField()
    category = models.TextField(blank=True, null=True)
    add_team_to_phrase = models.BooleanField()

    def __str__(self):
        return self.name
