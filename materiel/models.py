from django.db import models

class Tag(models.Model):
    departement_m = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.departement_m


class materiel(models.Model):
    ID_M = models.CharField(max_length=200, unique=True, null=True)
    departement = models.ManyToManyField(Tag)
    datedereception = models.DateField(auto_now_add=True)
    Nature = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.ID_M
