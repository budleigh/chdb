from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from chdb_app.models import *


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    base_model = Person
    readonly_fields = ['alive', 'id']  # life is governed by change.


# GROUP #
@admin.register(Government)
class GovernmentAdmin(PolymorphicChildModelAdmin):
    base_model = Government
    readonly_fields = ['id']


@admin.register(Group)
class GroupAdmin(PolymorphicParentModelAdmin):
    base_model = Group
    child_models = (Government,)


# LOCATION #
@admin.register(City)
class CityAdmin(PolymorphicChildModelAdmin):
    base_model = City
    readonly_fields = ['id']


@admin.register(Region)
class RegionAdmin(PolymorphicChildModelAdmin):
    base_model = Region
    readonly_fields = ['id']


@admin.register(Location)
class LocationAdmin(PolymorphicParentModelAdmin):
    base_model = Location
    child_models = (City, Region)


# EVENT #
@admin.register(War)
class WarAdmin(PolymorphicChildModelAdmin):
    base_model = War
    readonly_fields = ['id']


@admin.register(Battle)
class BattleAdmin(PolymorphicChildModelAdmin):
    base_model = Battle
    readonly_fields = ['id']


@admin.register(Event)
class EventAdmin(PolymorphicParentModelAdmin):
    base_model = Event
    child_models = (War, Battle)


# CHANGE #
@admin.register(BooleanFieldChange)
class BooleanFieldChangeAdmin(PolymorphicChildModelAdmin):
    base_model = BooleanFieldChange
    readonly_fields = ['id']


@admin.register(CharFieldChange)
class CharFieldChangeAdmin(PolymorphicChildModelAdmin):
    base_model = CharFieldChange
    readonly_fields = ['id']


@admin.register(FieldChange)
class FieldChangeAdmin(PolymorphicParentModelAdmin):
    base_model = FieldChange
    child_models = (
        CharFieldChange,
        BooleanFieldChange,
    )
