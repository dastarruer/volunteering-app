from django.db import models


# Create your models here.
class Opportunity(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    numTotalVolunteers = models.IntegerField()
    numSignedVolunteers = models.IntegerField()

    # To keep it simple, hardcode the location for now
    distanceFromUserKilometers = models.FloatField()

    def __str__(self):
        return self.title
