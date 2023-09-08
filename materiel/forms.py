from django.forms import ModelForm
from .models import materiel
from .models import Tag
from django import forms
class MaterielForm(forms.ModelForm):
    departement = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    class Meta:
        model = materiel
        fields = ['ID_M', 'departement']

    def clean_departement(self):
        departement = self.cleaned_data.get('departement')
        if not departement:
            raise forms.ValidationError("Le champ 'departement' ne peut pas être vide.")
        return departement