from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('cours/',views.cours, name='cours'),
    path('hackathon/',views.hackathon, name='hackathon'),
    path('youtube/',views.youtube, name='youtube'),
    path('Dev_Club_community/',views.Dev_Club_community, name='Dev_Club_community'),
    path('accueil/',views.accueil, name='accueil'),
    
]
