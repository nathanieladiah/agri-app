# Generated by Django 4.0.6 on 2022-07-28 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batch',
            options={'verbose_name_plural': 'batches'},
        ),
        migrations.AlterModelOptions(
            name='birds',
            options={'verbose_name_plural': 'eggs'},
        ),
        migrations.AlterModelOptions(
            name='eggs',
            options={'verbose_name_plural': 'eggs'},
        ),
        migrations.AlterModelOptions(
            name='feed',
            options={'verbose_name_plural': 'feed'},
        ),
    ]
