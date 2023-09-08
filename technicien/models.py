
from django.db import models

STATUS = (('Assigné', 'Assigné'),
          ('Libre', 'Libre'))

# Create your models here.
class technicien(models.Model):
    ID_T= models.CharField(max_length=200, unique=True,null=True)
    statuts = models.CharField(max_length=200, null=True, choices=STATUS)
    Nom=models.CharField(max_length=200,null=True)
    demandes_assignees = models.ManyToManyField('demande.Demande', related_name='techniciens_assignes', blank=True)
    def __str__(self) :
     return self.ID_T

