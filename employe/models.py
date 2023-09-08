from django.db import models

class employe(models.Model):
    ID_E = models.CharField(max_length=200, unique=True, null=True)
    nomE = models.CharField(max_length=200, null=True)
    departement = models.CharField(max_length=200, null=True)
    
    date_ajout = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.ID_E
