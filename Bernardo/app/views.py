from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .spotify import get_playlist_by_mood

class IndexPageView(TemplateView):
    template_name = 'app/index.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

def select_mood(request):
    return render(request, 'app/select_mood.html')

def mood_playlist(request, mood):
    playlists = get_playlist_by_mood(mood)  # Assume this function retrieves playlists based on the mood
    return render(request, 'app/mood_playlist.html', {'playlists': playlists, 'mood': mood})