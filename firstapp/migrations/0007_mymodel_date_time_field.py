# Generated by Django 5.0.6 on 2024-06-08 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_mymodel_date_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='date_time_field',
            field=models.DateTimeField(default=None),
        ),
    ]
