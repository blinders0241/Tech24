# Generated by Django 5.0 on 2024-02-04 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarFlix', '0006_ffmoviedetailsmodel_country_imdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ffmoviedetailsmodel',
            name='Watched',
            field=models.CharField(default='N', max_length=30),
        ),
    ]
