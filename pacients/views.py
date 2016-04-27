from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from doctors.models   import Doctor
from pacients.models  import Pacient
from pacients.forms import PacientForm


class PacientList(ListView):
    model = Pacient
    context_object_name = 'pacients'

class PacientDetail(DetailView):
    model = Pacient
    context_object_name = 'pacient'

class PacientCreate(CreateView):
    model = Pacient
    form_class = PacientForm
    context_object_name = 'form'
    success_url = '/pacients/'

    def get_context_data(self, **kwargs):
        context = super(PacientCreate, self).get_context_data(**kwargs)
        context['title'] = 'Registrar Paciente'
        context['button_name'] = 'Guardar'
        return context

class PacientUpdate(UpdateView):
    model = Pacient
    form_class = PacientForm
    context_object_name = 'form'
    success_url = '/pacients/'

    def get_context_data(self, **kwargs):
        context = super(PacientUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Editar Paciente'
        context['button_name'] = 'Editar'
        return context

class PacientDelete(DeleteView):
    model = Pacient
    success_url = reverse_lazy('show_pacients')