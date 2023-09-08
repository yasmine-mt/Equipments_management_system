from django.urls import path
from . import views
urlpatterns = [
    path('',views.list_demande),
    path('volet/', views.volet_view, name='volet'),
    path('xdemande/', views.xdemande,name='xdemande'),
    path('demande_reparation/', views.demande_reparation, name='demande_reparation'),
    path('demande_attribution/', views.demande_attribution, name='demande_attribution'),
    path('dt/', views.dt, name='dt'),
    path('demandeattribuer_materiel_employe/<int:demande_id>/', views.attribuer_materiel_employe,  name='attribuer_materiel_employe'),
    path('assigner_untec/<int:demande_id>/<int:technicien_id>/', views.assigner_untec, name='assigner_untec'),
    path('ajouter_dem/', views.ajouter_demande, name='ajouter_demande'),
    path('assignation/', views.demandesass, name='demandeass'),
    path('supprimer_demande/<str:demande_id>/', views.supprimer_demande, name='supprimer_demande'),

]