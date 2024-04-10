from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Movie

# data = {
#    'movies': [
#        {
#          'id': 5,
#          'title': 'Jaws',
#          'year': 1669,
#        },
#        {
#          'id': 6,
#          'title': 'Sharknado',
#          'year': 1600 ,
#        },
#        {
#          'id': 5,
#          'title': 'The Meg',
#          'year': 2000,
#        }
#    ]
# }

def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})

def home(request):
    return HttpResponse("Home page")

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movies': data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')

    return render(request, 'movies/add.html')

def delete(request, id):
    try:
     Movie.objects.get(pk=id).delete()
    except:
        raise Http404('Page not found')

    return HttpResponseRedirect('/movies')