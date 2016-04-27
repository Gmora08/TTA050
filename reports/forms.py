from django import forms
from .models import Report

class ReportCreateForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['image']

    def save(self, *args, **kwargs):
        self.instance.doctor = kwargs["doctor"]
        self.instance.pacient = kwargs["pacient"]
        #commit=kwargs["commit"]
        save_form = super(ReportCreateForm, self).save()
        return save_form

    

