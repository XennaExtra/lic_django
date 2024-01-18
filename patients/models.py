from django.db import models
from django.conf import Settings
from datetime import date
from django.core.validators import RegexValidator

class Patient(models.Model):
    patient_number = models.CharField(primary_key=True, max_length=6, validators=[RegexValidator(r'^\d{0,9}$')])
    patient_password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=False, default='Jerzy')
    second_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=False, default="Nowak")
    pesel_number = models.CharField(max_length=11, blank=False, default='00000000000', validators=[RegexValidator(r'^\d{0,9}$')])
    birth_date = models.DateField(default=date.today().strftime('%d-%m-%Y'))
    patient_phone = models.CharField(max_length=12, unique=True, blank=False, null=False)
    def __str__(self) -> str:
        return self.patient_number
