from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique trip instances

class Activity(models.Model):
    """Model representing an activity type"""
    name = models.CharField(max_length=200, help_text='Enter an activity type i.e. climbing')
    pin = models.ImageField(null=True,blank=True,upload_to="img/%y")

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
class CombinedTrip(models.Model):
    """Model for holding trips which are grouped"""
    name = models.CharField(max_length=200, help_text="Enter a name for the combined trip")
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        """Returns the URL to access a particular combined trip."""
        return reverse('combined trip', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
class Participents(models.Model):
    """Model representing Participents."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
    
class Trip(models.Model):
    """Model representing a specific trip"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular trip')
    name = models.CharField(max_length=200, help_text="Enter a name for the trip")
    combined_trip = models.ForeignKey('CombinedTrip', on_delete=models.RESTRICT, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    # Author is a string rather than an object because it hasn't been declared yet in the file
    activity = models.ManyToManyField('Activity')
    participents = models.ManyToManyField('Participents', null=True, blank=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the trip', blank=True, null=True)
    SEASON_LIST = (
        ('s', 'Summer'),
        ('a', 'Autaum'),
        ('w', 'Winter'),
        ('p', 'Spring'),
    )
    season = models.CharField(
        max_length=1,
        choices=SEASON_LIST,
        blank=True,
        default='s',
        help_text='Season',
    )
    future = models.BooleanField()
    weblink = models.URLField(blank=True)
    social_link = models.URLField(blank=True)
    track_file = models.FileField(blank=True, upload_to="tracks/%y")
    pin_location_lat = models.FloatField(blank=True, null=True)
    pin_location_lon = models.FloatField(blank=True, null=True)


    class Meta:
        ordering = ['date']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.name})'
    
    def display_activity(self):
        """Create a string for the Activity. This is required to display activity in Admin."""
        return ', '.join(activity.name for activity in self.activity.all()[:3])

    display_activity.short_description = 'Activity'
    
    #def display_combined_trip(self):
        #return ', '.join(combined_trip.name for day in self.combined_trip.all()[:3])

    #display_combined_trip.short_description = 'Combined trip'

    