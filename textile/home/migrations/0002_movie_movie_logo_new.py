# Generated by Django 2.1.4 on 2018-12-19 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_logo_new',
            field=models.CharField(default='', editable=False, max_length=70),
        ),
    ]
