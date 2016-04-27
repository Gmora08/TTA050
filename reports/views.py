from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, DetailView
from .utils import analize_image
from doctors.models import Doctor
from pacients.models import Pacient
from .models import Report
from .forms import ReportCreateForm

class ReportCreate(View):
    template_response = 'reports/report_form.html'
    def get(self, request, pk):
        form = ReportCreateForm()
        return render(request, self.template_response, {'form': form})

    def post(self, request, pk):
        form = ReportCreateForm(request.POST, request.FILES)
        if form.is_valid():
            doctor  =  Doctor.objects.get(user=self.request.user)
            pacient =  Pacient.objects.get(pk=pk)
            report = form.save(doctor=doctor, pacient=pacient, commit=False)
            print report.image.url
            data = analize_image(report.image.url)
            return redirect(reverse('index_pacients'))
        else:
            return render(request, self.template_response, {'form': form})

