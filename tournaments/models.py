from django.db import models
from django_countries.fields import CountryField, Country


class Player(models.Model):
    name = models.CharField(max_length=255, unique=True)
    age = models.IntegerField()
    rating = models.IntegerField()
    country = CountryField(default='Uz')

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    participants = models.ManyToManyField(Player)

    def __str__(self):
        return self.name
