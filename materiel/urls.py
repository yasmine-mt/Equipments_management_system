
from django.urls import path
from . import views
urlpatterns = [
    path('accueil',views.home,name='accueil'),
     path('dashboard/', views.dashboard, name='dashboard'),
    path('accueil2',views.accueil2,name='accueil2'),
    path('', views.accueil, name='page_accueil'),
    path('accueil_technicien/', views.home_technicien, name='accueil_technicien'),
    path('info_technicien/', views.technique, name='info_technicien'),
    path('signaler_reparation/<int:demande_id>/', views.signaler_reparation, name='signaler_reparation'),
    path('enreg_materiel/', views.enregistrer_materiel, name='enreg_materiel'),
    path('xmateriel/', views.xmateriel, name='xmateriel'),
]
