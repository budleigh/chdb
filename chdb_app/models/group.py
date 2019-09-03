from django.db import models
from chdb_app.models.base import Entity, CHDBDateModel


class Group(Entity):
    members = models.ManyToManyField('Person', through='GroupMembership')
    created = models.DateField()
    created_by_group = models.ForeignKey(
        'self', related_name='created_groups', on_delete=models.SET_NULL, null=True, blank=True
    )
    created_by_person = models.ForeignKey(
        'Person', related_name='created_groups', on_delete=models.SET_NULL, null=True, blank=True
    )
    created_by_people = models.ManyToManyField('Person', related_name='created_groups_with_others')
    created_at_location = models.ForeignKey(
        'Location', related_name='groups_created_at', on_delete=models.SET_NULL, null=True, blank=True
    )


class Government(Group):
    pass


class PoliticalGroup(Group):
    pass


class Corporation(Group):
    pass


class Alliance(Group):
    pass


class Army(Group):
    pass


class GroupHierarchyPosition(models.Model):
    group = models.ForeignKey('Group', related_name='hierarchy_positions', on_delete=models.CASCADE)
    ordinal = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=255)


class GroupMembership(CHDBDateModel):
    person = models.ForeignKey('Person', related_name='groups', on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    hierarchy_position = models.ForeignKey(GroupHierarchyPosition, on_delete=models.SET_NULL, null=True, blank=True)


class MetaGroupMembership(CHDBDateModel):
    meta_group = models.ForeignKey('Group', related_name='sub_groups', on_delete=models.CASCADE)
    group = models.ForeignKey('Group', related_name='meta_groups', on_delete=models.CASCADE)
