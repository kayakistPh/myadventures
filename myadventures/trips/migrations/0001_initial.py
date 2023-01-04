# Generated by Django 4.1.4 on 2022-12-19 22:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter an activity type i.e. climbing', max_length=200)),
                ('pin', models.ImageField(blank=True, null=True, upload_to='img/%y')),
            ],
        ),
        migrations.CreateModel(
            name='CombinedTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name for the combined trip', max_length=200)),
                ('date_start', models.DateField(blank=True, null=True)),
                ('date_end', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular trip', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter a name for the trip', max_length=200)),
                ('date', models.DateField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, help_text='Enter a brief description of the trip', max_length=1000, null=True)),
                ('season', models.CharField(blank=True, choices=[('s', 'Summer'), ('a', 'Autaum'), ('w', 'Winter'), ('p', 'Spring')], default='s', help_text='Season', max_length=1)),
                ('future', models.BooleanField()),
                ('weblink', models.URLField(blank=True)),
                ('social_link', models.URLField(blank=True)),
                ('track_file', models.FileField(blank=True, upload_to='tracks/%y')),
                ('pin_location_lat', models.FloatField(blank=True, null=True)),
                ('pin_location_lon', models.FloatField(blank=True, null=True)),
                ('activity', models.ManyToManyField(to='trips.activity')),
                ('combined_trip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='trips.combinedtrip')),
                ('participents', models.ManyToManyField(to='trips.participents')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]