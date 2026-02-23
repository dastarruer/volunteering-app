from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    upcoming_opportunities = models.ManyToManyField(
        "opportunities.Opportunity", blank=True, related_name="upcoming_by"
    )
    completed_opportunities = models.ManyToManyField(
        "opportunities.Opportunity", blank=True, related_name="completed_by"
    )
    streak = models.IntegerField(default=0)
    streak_last_updated = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
