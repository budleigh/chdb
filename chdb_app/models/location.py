from django.db import models
from chdb_app.models.base import Entity, CHDBDateModel


class Location(Entity):
    parent = models.ForeignKey('self', related_name='children', null=True, on_delete=models.SET_NULL, blank=True)
    people = models.ManyToManyField('Person', through='PersonAtLocation')


class City(Location):
    pass


class Region(Location):
    pass


class Continent(Location):
    pass


class District(Location):
    pass


class Address(Location):
    pass


class Place(Location):
    pass


class PersonAtLocation(CHDBDateModel):
    person = models.ForeignKey('Person', related_name='locations', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    ownership = models.BooleanField(default=False)


class GroupAtLocation(CHDBDateModel):
    group = models.ForeignKey('Group', related_name='locations', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    ownership = models.BooleanField(default=False)
