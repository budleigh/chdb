from django.db import models
from polymorphic.models import PolymorphicModel
from chdb_app.models.base import CHDBDateModel, Entity


class Event(Entity, CHDBDateModel):
    at_location = models.ForeignKey('Location', related_name='events', on_delete=models.SET_NULL, null=True, blank=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)


class PersonEventParticipation(PolymorphicModel, CHDBDateModel):
    person = models.ForeignKey('Person', related_name='events', on_delete=models.CASCADE)


class GroupEventParticipation(PolymorphicModel, CHDBDateModel):
    group = models.ForeignKey('Group', related_name='events', on_delete=models.CASCADE)


class MilitaryEvent(Event):
    casualties = models.PositiveIntegerField()
    groups = models.ManyToManyField('Group', through='GroupMilitaryEventParticipation')
    people = models.ManyToManyField('Person', through='PersonMilitaryEventParticipation')


class War(MilitaryEvent):
    pass


class Battle(MilitaryEvent):
    pass


class GroupMilitaryEventParticipation(GroupEventParticipation):
    event = models.ForeignKey('MilitaryEvent', on_delete=models.CASCADE)
    casualties = models.PositiveIntegerField()
    belligerent_ordinal = models.PositiveIntegerField()  # for grouping belligerent sides
    victory = models.BooleanField()


class PersonMilitaryEventParticipation(PersonEventParticipation):
    event = models.ForeignKey('MilitaryEvent', on_delete=models.CASCADE)
