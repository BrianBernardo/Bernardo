from django.urls import path
from .views import IndexPageView, AboutPageView, select_mood, mood_playlist

urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('select_mood/', select_mood, name='select_mood'),
    path('mood/<str:mood>/', mood_playlist, name='mood_playlist'),
]