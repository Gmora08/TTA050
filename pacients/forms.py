from django import forms
from .models import Pacient

class PacientForm(forms.ModelForm):
    class Meta:
        model = Pacient
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput()
        }

