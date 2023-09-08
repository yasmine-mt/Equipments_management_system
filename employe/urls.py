from django.urls import path
from . import views
urlpatterns = [
    path('/<str:pk>',views.list_employe,name='employe'),
    path('creer_employe/', views.creer_employe, name='creer_employe'),
    path('xemploye/', views.xemploye, name='xemploye'),
    path('demandeinfos/', views.demandeinfos,name='demandeinfos'),
    path('supprimer_employe/<str:pk>/', views.supprimer_employe, name='supprimer_employe'),
]