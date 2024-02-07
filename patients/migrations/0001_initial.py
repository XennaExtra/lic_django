# Generated by Django 5.0.1 on 2024-01-18 13:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_number', models.CharField(max_length=6, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{0,9}$')])),
                ('patient_password', models.CharField(max_length=100)),
                ('first_name', models.CharField(default='Jerzy', max_length=100)),
                ('second_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(default='Nowak', max_length=100)),
                ('pesel_number', models.CharField(default='00000000000', max_length=11, validators=[django.core.validators.RegexValidator('^\\d{0,9}$')])),
                ('birth_date', models.DateField(default='18-01-2024')),
                ('patient_phone', models.CharField(max_length=12, unique=True)),
            ],
        ),
    ]
