# Generated by Django 5.0.6 on 2024-06-08 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_mymodel_date_time_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='duration_field',
            field=models.DurationField(default=None),
        ),
    ]
