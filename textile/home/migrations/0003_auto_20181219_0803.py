# Generated by Django 2.1.4 on 2018-12-19 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_movie_movie_logo_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_logo_new',
            field=models.CharField(default='', max_length=70),
        ),
    ]
