from django.db import models

class Mix(models.Model):
    date_submitted = models.DateField()
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=200)

    # The character string used to look up this mix
    url_identifier = models.CharField(max_length=50)

    def __str__(self):
        return "<Mix name=%s>" % self.name


class Track(models.Model):
    mix = models.ForeignKey(Mix)
    # MBID is exactly 36 chars long
    # TODO: Somehow get a minimum length
    musicbrainz_id = models.CharField(max_length=36)
    order = models.PositiveIntegerField()
    note = models.TextField()
