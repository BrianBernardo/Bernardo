from django.urls import path
from .views import IndexPageView, AboutPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]