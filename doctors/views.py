from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from .forms import DoctorForm
from . import models

def create(request):
	template_response = 'new.html'
	if request.method == 'POST':
		doctor_form = DoctorForm(request.POST)
		user_form = UserCreationForm(request.POST)
		if doctor_form.is_valid():
			user = form.save()
			doctor = form.save(user)
			#Return to login url
			pass
		else:
			return render(request, template_response, {'form': doctor_form})

	else:
		doctor_form = DoctorForm()
		return render(request, template_response, {'form': doctor_form})

def login(request):
	template_response = 'login.html'
    if request.method=='POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            #return to show pacients
            pass
        else:
            messages.error(request, u'Usuario/Password incorrecto')
            return render(request, template_response, {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, template_response, {'form': form})