from django.db import models
from chdb_app.models.base import Entity


class Person(Entity):
    born_at = models.ForeignKey('Location', related_name='births', on_delete=models.SET_NULL, null=True, blank=True)
    born_on = models.DateField()
    alive = models.BooleanField(default=True)  # everyone starts out this way lol
