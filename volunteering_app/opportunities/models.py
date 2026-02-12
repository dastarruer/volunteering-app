from django.db import models


# Create your models here.
class Opportunity(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="opportunities/", null=True, blank=True)
    num_total_volunteers = models.IntegerField()
    num_signed_volunteers = models.IntegerField()

    # To keep it simple, hardcode the location for now
    distance_from_user_km = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        # Without this, the admin panel will show 'Opportunitys'
        verbose_name_plural = "Opportunities"
