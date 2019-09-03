from django.db import models
from chdb_app.models.base import Entity


class Object(Entity):
    pass


class Ship(Object):
    engine_type = models.CharField(max_length=15, choices=(
        ('STEAM', 'Steam'),
        ('NUCLEAR', 'Nuclear'),
        ('SAIL', 'Sail'),
    ))
