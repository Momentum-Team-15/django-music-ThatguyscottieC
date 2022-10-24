from django.shortcuts import render, redirect
from django.views.generic import ListView
from music.forms import AlbumForm
from .models import Album


# Create your views here.


def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})


def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'music/album_detail.html', {'album': album})


class HomePageView(ListView):
    model = Album
    template_name = "base.html"


def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return redirect("home")
    else:
        form = AlbumForm()
    return render(request, 'music/create_album.html', {'form': form})
