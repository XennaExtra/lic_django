from django.db import models
from django.conf import Settings
class Examination(models.Model):
    name = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=100, blank=False)
    est_time_needed = models.PositiveIntegerField(default=0, blank=False)

    def __str__(self) -> str:
        return self.name

class Outpost(models.Model):
    outpost_name = models.CharField(max_length=200, blank=False, default="Name")
    city = models.CharField(max_length=100, blank=False)
    street = models.CharField(max_length=100, blank=False)
    building = models.PositiveIntegerField(default=1, blank=False)
    premise = models.PositiveIntegerField(default=1, blank=True, null=True)
    phone_number = models.CharField(max_length=12, unique=True, blank=False, null=False)
    def __str__(self) -> str:
        return self.outpost_name
