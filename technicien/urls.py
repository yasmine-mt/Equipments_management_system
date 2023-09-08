from django.urls import path
from . import views
urlpatterns = [
    path('',views.list_technicien),
    path('ajout_technicien/',views.ajouter_technicien,name='ajout_technicien'),
    path('xtechnicien/', views.xtechnicien, name='xtechnicien'),
    path('supprimer_technicien/<str:pk>/', views.supprimer_technicien, name='supprimer_technicien'),



]