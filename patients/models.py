from django.db import models
from users.models import CustomUser


class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    patient_number = models.CharField(max_length=6, unique=True, blank=False, null=False)
    full_name = models.CharField(max_length=100, unique=False, blank=False, null=False)
    birth_date = models.DateField(unique=False, blank=False, null=False)
    pesel_number = models.CharField(max_length=11, unique=True, blank=False, null=False)

    def __str__(self):
        return self.patient_number
