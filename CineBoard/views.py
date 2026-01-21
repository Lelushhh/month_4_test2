from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from CineBoard.models import Movies, Reviews
from .forms import MovieForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import logout

from django.db.models import Q

def movie(request):
    query = request.GET.get('q')
    genre = request.GET.get('genre')

    movies = Movies.objects.all().order_by('-created_at')

    if query:
        movies = movies.filter(
            Q(name_movie__icontains=query) |
            Q(description__icontains=query)
        )

    if genre:
        movies = movies.filter(jenre_movies=genre)

    return render(request, 'movie/movie_list.html', {
        'movies': movies,
        'current_genre': genre,
        'query': query
    })

def logout_view(request):
    logout(request)
    return redirect('login')




def movie_detail(request, id):
    movie = get_object_or_404(Movies, id=id)
    reviews = Reviews.objects.filter(choice_movie=movie).order_by('-created_at')

    if request.method == 'POST' and request.user.is_authenticated:
        text = request.POST.get('text')
        marks = request.POST.get('marks')

        if text and marks:
            Reviews.objects.create(
                choice_movie=movie,
                text=text,
                marks=marks
            )

        return redirect('movie_detail', id=movie.id)

    return render(
        request,
        'movie/movie_detail.html',
        {
            'movie': movie,
            'reviews': reviews
        }
    )




@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie')
    else:
        form = MovieForm()

    return render(request, 'movie/movie_create.html', {'form': form})