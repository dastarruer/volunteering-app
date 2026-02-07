from django.db import models


# Create your models here.
class Opportunity(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="opportunities/", null=True, blank=True)
    numTotalVolunteers = models.IntegerField()
    numSignedVolunteers = models.IntegerField()

    # To keep it simple, hardcode the location for now
    distanceFromUserKilometers = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        # Without this, the admin panel will show 'Opportunitys'
        verbose_name_plural = "Opportunities"
