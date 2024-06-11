# Generated by Django 5.0 on 2024-04-06 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equityHome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexHistoricalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('INDEXNAME', models.CharField(default=None, max_length=120)),
                ('OPEN', models.FloatField(default=0.0)),
                ('HIGH', models.FloatField(default=0.0)),
                ('LOW', models.FloatField(default=0.0)),
                ('CLOSE', models.FloatField(default=0.0)),
                ('TOTTRDQTY', models.CharField(default=None, max_length=120)),
                ('TOTTRDVAL', models.CharField(blank=True, default=None, editable=False, max_length=120, null=True)),
                ('TIMESTAMP', models.CharField(default=None, max_length=120)),
            ],
        ),
    ]
