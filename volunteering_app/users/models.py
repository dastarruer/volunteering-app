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
