from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from polymorphic.models import PolymorphicModel


class FieldChange(PolymorphicModel):
    """
    Changes encode a difference in a model's properties by way of time.
    These tables are meant to convey an idea such as "on July 4th,
    1776, the American Colonies became the United States".

    Instead of making a 'union change type' with all possible field types
    on it, we made individual field change tables to make it much more
    space efficient.
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    changed_object = GenericForeignKey('content_type', 'object_id')
    # it appears that polymorphic confuses the contenttypes framework
    # it looks for content_type no matter what, so keep above naming
    changed_property_str = models.CharField(max_length=255, db_index=True)
    date_changed = models.DateField()
    caused_by_event = models.ForeignKey(
        'Event', related_name='caused_changes', on_delete=models.SET_NULL, null=True, blank=True
    )
    caused_by_change = models.ForeignKey(
        'self', related_name='caused_changes', on_delete=models.SET_NULL, null=True, blank=True
    )
    caused_by_group = models.ForeignKey(
        'Group', related_name='caused_changes', on_delete=models.SET_NULL, null=True, blank=True
    )
    caused_by_person = models.ForeignKey(
        'Person', related_name='caused_changes', on_delete=models.SET_NULL, null=True, blank=True
    )
    change_location = models.ForeignKey(
        'Location', related_name='changes_here', on_delete=models.SET_NULL, null=True, blank=True
    )


class CharFieldChange(FieldChange):
    changed_property_val = models.CharField(max_length=255, db_index=True)


class BooleanFieldChange(FieldChange):
    changed_property_val = models.BooleanField()


class FloatFieldChange(FieldChange):
    changed_property_val = models.FloatField()


class IntegerFieldChange(FieldChange):
    changed_property_val = models.IntegerField()


class PositiveIntegerFieldChange(FieldChange):
    changed_property_val = models.PositiveIntegerField()


class TextFieldChange(FieldChange):
    changed_property_val = models.TextField()


class ForeignKeyChange(FieldChange):
    foreign_key_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    foreign_key_id = models.PositiveIntegerField()
    foreign_object = GenericForeignKey('foreign_key_type', 'foreign_key_id')


class BaseTransition(PolymorphicModel):
    """
    Transitions are meant to convey the meaning of one object becoming another. This is
    specifically meant to be used when an object becomes a different TYPE of object.
    All other changes should be communicable as property changes.
    """
    date_changed = models.DateField()
    caused_by_event = models.ForeignKey(
        'Event', related_name='caused_transitions', on_delete=models.SET_NULL, null=True, blank=True
    )
    caused_by_change = models.ForeignKey(
        'self', related_name='caused_transitions', on_delete=models.SET_NULL, null=True, blank=True
    )
    caused_by_group = models.ForeignKey(
        'Group', related_name='caused_transitions', on_delete=models.SET_NULL, null=True, blank=True
    )
    caused_by_person = models.ForeignKey(
        'Person', related_name='caused_transitions', on_delete=models.SET_NULL, null=True, blank=True
    )
    change_location = models.ForeignKey(
        'Location', related_name='transitions_here', on_delete=models.SET_NULL, null=True, blank=True
    )


class FullObjectTransition(BaseTransition):
    """
    Encodes a change where one object becomes a completely different type of object.
    """
    original_object_type = models.ForeignKey(
        ContentType, related_name='original_type_for_object_transition', on_delete=models.CASCADE
    )
    original_object_id = models.PositiveIntegerField()
    original_object = GenericForeignKey('original_object_type', 'original_object_id')
    new_object_type = models.ForeignKey(
        ContentType, related_name='new_type_for_object_transition', on_delete=models.CASCADE
    )
    new_object_id = models.PositiveIntegerField()
    new_object = GenericForeignKey('new_object_type', 'new_object_id')


class FullObjectSplit(BaseTransition):
    """
    Encodes a change where one object becomes several completely different objects.
    """
    original_object_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    original_object_id = models.PositiveIntegerField()
    original_object = GenericForeignKey('original_object_type', 'original_object_id')


class FullObjectSplitResult(models.Model):
    """
    Links objects that resulted from splits to their original objects by way of the
    split object.
    """
    split = models.ForeignKey('FullObjectSplit', related_name='results', on_delete=models.CASCADE)
    result_object_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    result_object_id = models.PositiveIntegerField()
    result_object = GenericForeignKey('result_object_type', 'result_object_id')
