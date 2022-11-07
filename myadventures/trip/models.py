from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.user.id, filename)


class trip(models.Model):
    #  Pin logos
    default_pin = ""
    kayaking = ""
    walking = ""
    climbing = ""
    sightseeing = ""
    pin_logo_choices = [
        (default_pin, "Default pin"),
        (kayaking, "Kayaking"),
        (walking, "Hiking"),
        (climbing, "Climbing"),
        (sightseeing, "Sight seeing"),
    ]
    name = models.CharField(max_length=255)
    date = models.DateField(blank=True)
    pin_logo = models.CharField(
        max_length=255, choices=pin_logo_choices, default=default_pin
    )
    future = models.BooleanField()
    weblink = models.URLField(blank=True)
    social_link = models.URLField(blank=True)
    track_file = models.FileField(blank=True, upload_to=user_directory_path)
    description = models.TextField(blank=True)
    # List/ tag like fields
    # tags = models.#####Needs to be a list like item
    # people = models.#####Needs to be a list like item
    # photos= models.#####Needs to be a list like item
    # https://dev.to/thepylot/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704

    # Populated fields these do not need to be filled out at the start but include them in the calss
    elevation = []
    track = []
    pin_location_lat = 0.0
    pin_location_long = 0.0
    map_zoom = 1

    # Extras to add later
    # Seasons
    # pin_photo
