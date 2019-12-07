# Generated by Django 2.2.7 on 2019-12-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20191204_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='preferred_genres',
            field=models.ManyToManyField(blank=True, to='movies.Genre'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='preferred_providers',
            field=models.ManyToManyField(blank=True, to='movies.Provider'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='watchlist',
            field=models.ManyToManyField(blank=True, to='movies.Movie'),
        ),
    ]