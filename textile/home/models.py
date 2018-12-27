from django.db import models
from froala_editor.fields import FroalaField
from django.urls import reverse
# Create your models here.

class Movie (models.Model):
    actor = models.CharField(max_length=30)
    actor_movie=models.CharField(max_length=50)
    genre=FroalaField()
    movie_logo=models.CharField(max_length=100)
    movie_logo_new=models.ImageField(upload_to='xyz',default='default2222.jpg')
    def get_absolute_url(self):
       ## return reverse('movie:detail',kwargs={'pk': self.pk})
       return reverse('movie:detail',kwargs={'movie_id': self.pk}) 

    def __str__(self):
        return self.actor + '_______' +self.actor_movie
class Song(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=50)
    songs_name=models.CharField(max_length=100)
    is_favorite=models.BooleanField(default=False)
    def __str__(self):
        return self.songs_name + '_______' +self.songs_name