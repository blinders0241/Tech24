# Generated by Django 5.0 on 2024-04-06 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equityHome', '0002_indexhistoricalmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexhistoricalmodel',
            name='TIMESTAMP',
            field=models.DateTimeField(default=None),
        ),
    ]
