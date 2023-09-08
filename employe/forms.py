from django.forms import ModelForm
from .models import employe
class EmployeForm(ModelForm):
    class Meta:
        model=employe
        fields='__all__'
