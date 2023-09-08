from django.forms import ModelForm
from .models import technicien
class TechnicienForm(ModelForm):
    class Meta:
        model=technicien
        fields='__all__'
