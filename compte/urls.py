from django.urls import path
from . import views
from django.contrib.auth.forms import UserCreationForm
urlpatterns = [
    path('acces', views.accesPage, name='acces'),
    path('acces_emp', views.accesPage2, name='acces_emp'),
    path('acces_tech', views.accesPage3, name='acces_tech'),
    path('choix-espace/', views.choix_espace, name='choix_espace'),
    path('Quitter', views.logoutUser, name='Quitter'),
]
