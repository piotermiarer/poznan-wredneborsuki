from django.db import models


class Team(models.Model):

    name = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.name
