from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ['user',]

    def save(self, user=None):
        self.instance.user = user
        super(DoctorForm, self).save()




