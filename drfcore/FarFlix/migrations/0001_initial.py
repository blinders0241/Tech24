# Generated by Django 5.0 on 2024-01-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarFlixMoviesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FilePath', models.CharField(default=None, max_length=220)),
                ('movieName_Disk', models.CharField(default=None, max_length=220)),
                ('FileSize', models.FloatField(default=0.0)),
                ('FileType', models.CharField(default=None, max_length=20)),
                ('movieCode_IMDB', models.CharField(default=None, max_length=30)),
                ('Title_IMDB', models.CharField(default=None, max_length=190)),
                ('Year_IMDB', models.CharField(default=None, max_length=30)),
                ('Genres_IMDB', models.CharField(default=None, max_length=130)),
                ('Classified', models.CharField(default=None, max_length=100)),
            ],
        ),
    ]
