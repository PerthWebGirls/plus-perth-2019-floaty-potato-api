# Generated by Django 2.2.7 on 2019-12-03 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=10)),
                ('image', models.ImageField(default='no-img.png', upload_to='classifications/')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='no-img.png', upload_to='genres/')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=5000)),
                ('duration', models.DurationField(blank=True)),
                ('release_date', models.DateField(blank=True)),
                ('image', models.ImageField(default='no-img.png', upload_to='movies/')),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movies.Classification')),
                ('genre', models.ManyToManyField(to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField(blank=True)),
                ('image', models.ImageField(default='no-img.png', upload_to='providers/')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(max_length=8, null=True)),
                ('avatar', models.ImageField(default='popcorn.jpg', null=True, upload_to='avatar/')),
                ('preferred_genres', models.ManyToManyField(to='movies.Genre')),
                ('preferred_providers', models.ManyToManyField(to='movies.Provider')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('watchlist', models.ManyToManyField(to='movies.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='provider',
            field=models.ManyToManyField(to='movies.Provider'),
        ),
    ]
