import django_filters
from .models import demande
class DemandeFiltre(django_filters.FilterSet):
    class Meta:
        model=demande
        fields='__all__'
        exclude=['technicien','employe' ,'date_creation', 'materiel']