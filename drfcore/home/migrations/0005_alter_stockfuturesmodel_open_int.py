# Generated by Django 5.0 on 2024-01-12 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_stockfuturesmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockfuturesmodel',
            name='OPEN_INT',
            field=models.FloatField(default=None, max_length=120),
        ),
    ]
