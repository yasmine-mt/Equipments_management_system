from django.db import models
from employe.models import employe
from materiel.models import materiel
from technicien.models import technicien
# Create your models here.
class demande(models.Model):
    STATUS = ((' traitée', ' traitée'),
                  ('en cours', 'en cours'),
                  ('non traitée', 'non traitée'))
    TYPE = ((' Réparation', ' Réparation'),
                ('Attribution', 'Attribution'))

    employe = models.ForeignKey(employe, null=True, on_delete=models.CASCADE)
    materiel = models.ForeignKey(materiel, null=True, on_delete=models.SET_NULL)
    technicien = models.ForeignKey(technicien, null=True, blank=True, on_delete=models.SET_NULL)
    ID_D = models.CharField(max_length=200, unique=True, null=True)
    type = models.CharField(max_length=200, null=True, choices=TYPE)
    date_creation = models.DateField(auto_now_add=True)
    statuts = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
      return self.ID_D
