# Generated by Django 2.2.4 on 2019-09-03 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseTransition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_changed', models.DateField()),
                ('caused_by_change', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='caused_transitions', to='chdb_app.BaseTransition')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_chdb_app.basetransition_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_chdb_app.entity_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='FieldChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('changed_property_str', models.CharField(db_index=True, max_length=255)),
                ('date_changed', models.DateField()),
                ('caused_by_change', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='caused_changes', to='chdb_app.FieldChange')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_chdb_app.fieldchange_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='GroupEventParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('date_to', models.DateField(blank=True, null=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_chdb_app.groupeventparticipation_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='GroupHierarchyPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordinal', models.PositiveIntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BooleanFieldChange',
            fields=[
                ('fieldchange_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.FieldChange')),
                ('changed_property_val', models.BooleanField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.fieldchange',),
        ),
        migrations.CreateModel(
            name='CharFieldChange',
            fields=[
                ('fieldchange_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.FieldChange')),
                ('changed_property_val', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.fieldchange',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Entity')),
                ('date', models.DateField(blank=True, null=True)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('date_to', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.entity', models.Model),
        ),
        migrations.CreateModel(
            name='FloatFieldChange',
            fields=[
                ('fieldchange_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.FieldChange')),
                ('changed_property_val', models.FloatField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.fieldchange',),
        ),
        migrations.CreateModel(
            name='FullObjectSplit',
            fields=[
                ('basetransition_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.BaseTransition')),
                ('original_object_id', models.PositiveIntegerField()),
                ('original_object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.basetransition',),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Entity')),
                ('created', models.DateField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.entity',),
        ),
        migrations.CreateModel(
            name='GroupMilitaryEventParticipation',
            fields=[
                ('groupeventparticipation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.GroupEventParticipation')),
                ('casualties', models.PositiveIntegerField()),
                ('belligerent_ordinal', models.PositiveIntegerField()),
                ('victory', models.BooleanField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.groupeventparticipation',),
        ),
        migrations.CreateModel(
            name='IntegerFieldChange',
            fields=[
                ('fieldchange_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.FieldChange')),
                ('changed_property_val', models.IntegerField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.fieldchange',),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Entity')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='chdb_app.Location')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.entity',),
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Entity')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.entity',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Entity')),
                ('born_on', models.DateField()),
                ('alive', models.BooleanField(default=True)),
                ('born_at', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='births', to='chdb_app.Location')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.entity',),
        ),
        migrations.CreateModel(
            name='PositiveIntegerFieldChange',
            fields=[
                ('fieldchange_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.FieldChange')),
                ('changed_property_val', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.fieldchange',),
        ),
        migrations.CreateModel(
            name='TextFieldChange',
            fields=[
                ('fieldchange_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.FieldChange')),
                ('changed_property_val', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.fieldchange',),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('location_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Location')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.location',),
        ),
        migrations.CreateModel(
            name='Alliance',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Group')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.group',),
        ),
        migrations.CreateModel(
            name='Army',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Group')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.group',),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('location_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Location')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.location',),
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('location_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Location')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.location',),
        ),
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Group')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.group',),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('location_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Location')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.location',),
        ),
        migrations.CreateModel(
            name='Government',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Group')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.group',),
        ),
        migrations.CreateModel(
            name='MilitaryEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Event')),
                ('casualties', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.event',),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('location_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Location')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.location',),
        ),
        migrations.CreateModel(
            name='PoliticalGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Group')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.group',),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('location_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Location')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.location',),
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('object_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.Object')),
                ('engine_type', models.CharField(choices=[('STEAM', 'Steam'), ('NUCLEAR', 'Nuclear'), ('SAIL', 'Sail')], max_length=15)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.object',),
        ),
        migrations.CreateModel(
            name='PersonEventParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('date_to', models.DateField(blank=True, null=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_chdb_app.personeventparticipation_set+', to='contenttypes.ContentType')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='chdb_app.Person')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='PersonAtLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('date_to', models.DateField(blank=True, null=True)),
                ('ownership', models.BooleanField(default=False)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chdb_app.Location')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='chdb_app.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MetaGroupMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('date_to', models.DateField(blank=True, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meta_groups', to='chdb_app.Group')),
                ('meta_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_groups', to='chdb_app.Group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='location',
            name='people',
            field=models.ManyToManyField(through='chdb_app.PersonAtLocation', to='chdb_app.Person'),
        ),
        migrations.CreateModel(
            name='GroupMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('date_to', models.DateField(blank=True, null=True)),
                ('hierarchy_position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chdb_app.GroupHierarchyPosition')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chdb_app.Group')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='chdb_app.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='grouphierarchyposition',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hierarchy_positions', to='chdb_app.Group'),
        ),
        migrations.AddField(
            model_name='groupeventparticipation',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='chdb_app.Group'),
        ),
        migrations.CreateModel(
            name='GroupAtLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('date_to', models.DateField(blank=True, null=True)),
                ('ownership', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='chdb_app.Group')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chdb_app.Location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='group',
            name='created_at_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groups_created_at', to='chdb_app.Location'),
        ),
        migrations.AddField(
            model_name='group',
            name='created_by_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_groups', to='chdb_app.Group'),
        ),
        migrations.AddField(
            model_name='group',
            name='created_by_people',
            field=models.ManyToManyField(related_name='created_groups_with_others', to='chdb_app.Person'),
        ),
        migrations.AddField(
            model_name='group',
            name='created_by_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_groups', to='chdb_app.Person'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='chdb_app.GroupMembership', to='chdb_app.Person'),
        ),
        migrations.CreateModel(
            name='FullObjectTransition',
            fields=[
                ('basetransition_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.BaseTransition')),
                ('original_object_id', models.PositiveIntegerField()),
                ('new_object_id', models.PositiveIntegerField()),
                ('new_object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new_type_for_object_transition', to='contenttypes.ContentType')),
                ('original_object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original_type_for_object_transition', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.basetransition',),
        ),
        migrations.CreateModel(
            name='FullObjectSplitResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_object_id', models.PositiveIntegerField()),
                ('result_object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('split', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='chdb_app.FullObjectSplit')),
            ],
        ),
        migrations.CreateModel(
            name='ForeignKeyChange',
            fields=[
                ('fieldchange_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.FieldChange')),
                ('foreign_key_id', models.PositiveIntegerField()),
                ('foreign_key_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.fieldchange',),
        ),
        migrations.AddField(
            model_name='fieldchange',
            name='caused_by_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='caused_changes', to='chdb_app.Event'),
        ),
        migrations.AddField(
            model_name='fieldchange',
            name='caused_by_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='caused_changes', to='chdb_app.Group'),
        ),
        migrations.AddField(
            model_name='fieldchange',
            name='caused_by_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='caused_changes', to='chdb_app.Person'),
        ),
        migrations.AddField(
            model_name='fieldchange',
            name='change_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='changes_here', to='chdb_app.Location'),
        ),
        migrations.AddField(
            model_name='event',
            name='at_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='chdb_app.Location'),
        ),
        migrations.AddField(
            model_name='event',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='chdb_app.Event'),
        ),
        migrations.AddField(
            model_name='basetransition',
            name='caused_by_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='caused_transitions', to='chdb_app.Event'),
        ),
        migrations.AddField(
            model_name='basetransition',
            name='caused_by_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='caused_transitions', to='chdb_app.Group'),
        ),
        migrations.AddField(
            model_name='basetransition',
            name='caused_by_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='caused_transitions', to='chdb_app.Person'),
        ),
        migrations.AddField(
            model_name='basetransition',
            name='change_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transitions_here', to='chdb_app.Location'),
        ),
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('militaryevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.MilitaryEvent')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.militaryevent',),
        ),
        migrations.CreateModel(
            name='War',
            fields=[
                ('militaryevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.MilitaryEvent')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.militaryevent',),
        ),
        migrations.CreateModel(
            name='PersonMilitaryEventParticipation',
            fields=[
                ('personeventparticipation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chdb_app.PersonEventParticipation')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chdb_app.MilitaryEvent')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('chdb_app.personeventparticipation',),
        ),
        migrations.AddField(
            model_name='militaryevent',
            name='groups',
            field=models.ManyToManyField(through='chdb_app.GroupMilitaryEventParticipation', to='chdb_app.Group'),
        ),
        migrations.AddField(
            model_name='militaryevent',
            name='people',
            field=models.ManyToManyField(through='chdb_app.PersonMilitaryEventParticipation', to='chdb_app.Person'),
        ),
        migrations.AddField(
            model_name='groupmilitaryeventparticipation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chdb_app.MilitaryEvent'),
        ),
    ]
