from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=255, unique=True)

    # Use full_name as username
    USERNAME_FIELD = "full_name"

    upcoming_opportunities = models.ManyToManyField(
        "opportunities.Opportunity", blank=True, related_name="upcoming_by"
    )
    completed_opportunities = models.ManyToManyField(
        "opportunities.Opportunity", blank=True, related_name="completed_by"
    )

    def __str__(self):
        return self.full_name
