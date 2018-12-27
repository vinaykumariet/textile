from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
#from django.http import HttpResponse
# from django.http import Http404
from .models import Movie,Song
from django.template import loader

# Create your views here.

class MovieCreateView(CreateView):
    model=Movie
    template_name = "movie/movie_form.html"
    fields={'actor','actor_movie','movie_logo'}
 


def index (request):
    all_movie=Movie.objects.all()
    # template=loader.get_template('movie/index.html')
    context={
        'all_movie':all_movie,
    }
    # html=''
    # all_movie=Movie.objects.all()
    # for a in all_movie:
    #     html+= str(a.id)
    
    # return HttpResponse(template.render(context, request))
    return render(request,'movie/index.html',context)


def details (request,movie_id):
    a1=get_object_or_404(Movie,pk=movie_id)
    # try:
    #     a1=Movie.objects.get(pk=movie_id)
    # except Movie.DoesNotExist:
    #     raise Http404("Not found")
    return render(request,'movie/detail.html',{'a1':a1})


def favorites (request,movie_id):
    a1=get_object_or_404(Movie,pk=movie_id)
    try:
        selected_song=a1.song_set.get(pk=request.POST['song'])
    except (KeyError,Song.DoesNotExist):
       return render(request,'movie/detail.html',{'a1':a1,'error_message': "not selected"}) 
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request,'movie/detail.html',{'a1':a1})
           
    # try:
    #     a1=Movie.objects.get(pk=movie_id)
    # except Movie.DoesNotExist:
    #     raise Http404("Not found")
    