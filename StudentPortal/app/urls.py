from django.urls import path
from . import views

urlpatterns = [
    path('Space/',views.home, name='studentSpace'),
    path('cours/',views.cours, name='courses'),
    path('hackathon/',views.hackathon, name='hackathon'),
    path('youtube/',views.youtube, name='youtube'),
    path('Dev/',views.Dev, name='Dev'),
    path('accueil/',views.accueil, name='accueil'),
    path('newbase/',views.newbase, name='newbase'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('enter/',views.enter, name= 'enter'),
]
