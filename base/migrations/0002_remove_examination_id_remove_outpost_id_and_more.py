# Generated by Django 5.0.1 on 2024-01-02 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examination',
            name='id',
        ),
        migrations.RemoveField(
            model_name='outpost',
            name='id',
        ),
        migrations.AddField(
            model_name='examination',
            name='examination_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='outpost',
            name='outpost_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='outpost',
            name='premise',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]
