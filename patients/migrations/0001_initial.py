# Generated by Django 5.0 on 2024-02-09 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_number', models.CharField(max_length=6, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('pesel_number', models.CharField(max_length=11, unique=True)),
            ],
        ),
    ]
