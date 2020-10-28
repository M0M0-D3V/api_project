from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mtg', views.mtg, name='mtg'),
    path('pokedex', views.pokedex, name="pokedex")
]
