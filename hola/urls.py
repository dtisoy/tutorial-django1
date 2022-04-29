from django.urls import path
from . import views

urlpatterns = [
    path("", views.hola, name='hola'),
    path("vader/", views.vader, name='hello vader'),
    path("<str:nombre>/", views.starwars, name="starwars") # getting a variable from the url
]
