from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from polymorphic.models import PolymorphicModel


class Entity(PolymorphicModel):
    """
    The base model here provides all other models with change-related access
    and functionality. It is important that changes be made and managed through
    this inherited interface so that things like change-clashes etc. can be
    properly detected and prevented.
    """
    name = models.CharField(max_length=255, db_index=True)
    changes = GenericRelation('FieldChange')

    def __str__(self):
        return self.name


class CHDBDateModel(models.Model):
    date = models.DateField(null=True, blank=True)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True
