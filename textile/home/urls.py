from django.urls import path,re_path
from .import views
app_name='movie'
urlpatterns = [
    path(r'', views.index),
    re_path(r'^(?P<movie_id>[0-9]+)/$', views.details,name='detail'),
     re_path(r'^(?P<movie_id>[0-9])+/favorites/$', views.favorites,name='favorite'),
      path(r'movie-add/', views.MovieCreateView.as_view()),
     
    
]