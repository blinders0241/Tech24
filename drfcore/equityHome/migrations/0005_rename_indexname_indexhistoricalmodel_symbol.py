# Generated by Django 5.0 on 2024-04-07 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equityHome', '0004_alter_indexhistoricalmodel_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indexhistoricalmodel',
            old_name='INDEXNAME',
            new_name='SYMBOL',
        ),
    ]
