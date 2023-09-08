from django import forms
from .models import demande

class DemandeForm(forms.ModelForm):
    class Meta:
        model = demande
        exclude = ['technicien']
        labels = {
            'employe': 'ID Employe',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['statuts'].initial = 'non traitée'  # Valeur initiale pour le champ statuts
        self.fields['employe'].initial = '1'
