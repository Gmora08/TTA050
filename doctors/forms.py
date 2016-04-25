from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm)
	def save(self, user=None):
   	    self.instace.user = user
    	super(DoctorForm, self).save()

 	class Meta:
        model = Doctor
        exclude = ['user',]


