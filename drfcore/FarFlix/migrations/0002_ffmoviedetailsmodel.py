# Generated by Django 5.0 on 2024-02-01 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarFlix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FFMovieDetailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title_IMDB', models.CharField(default=None, max_length=190)),
                ('Year_IMDB', models.CharField(default=None, max_length=30)),
                ('Genres_IMDB', models.CharField(default=None, max_length=130)),
                ('Directors_IMDB', models.CharField(default=None, max_length=130)),
                ('Writers_IMDB', models.CharField(default=None, max_length=230)),
                ('Cast_IMDB', models.CharField(default=None, max_length=330)),
                ('Plot_IMDB', models.CharField(default=None, max_length=2030)),
                ('Runtime_IMDB', models.CharField(default=None, max_length=130)),
                ('Language_IMDB', models.CharField(default=None, max_length=130)),
                ('Awards_IMDB', models.CharField(default=None, max_length=130)),
                ('Rating_IMDB', models.CharField(default=None, max_length=30)),
                ('MovieCode_IMDB', models.CharField(default=None, max_length=30)),
            ],
        ),
    ]
