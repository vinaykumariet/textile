# Generated by Django 2.1.4 on 2018-12-21 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20181220_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_logo_new',
            field=models.ImageField(default='default2222.jpg', upload_to='xyz'),
        ),
    ]