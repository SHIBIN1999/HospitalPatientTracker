from django.forms import ModelForm
from . models import patient


class PatientForm(ModelForm):
    class Meta:
        model=patient
        fields='__all__'