from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from .forms import DoctorForm

def create(request):
    template_response = 'doctors/new.html'
    if request.method == 'POST':
        doctor_form = DoctorForm(request.POST)
        user_data = request.POST.copy()
        user_data.update({'username': request.POST.get('email')})
        user_form = UserCreationForm(user_data)
        if doctor_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            doctor = doctor_form.save(user)
            return redirect(reverse('login'))
        else:
            print user_form.errors
            return render(request, template_response, {'form': doctor_form, 'user_form': user_form})

    else:
        user_form = UserCreationForm()
        doctor_form = DoctorForm()
        return render(request, template_response, {'form': doctor_form, 'user_form': user_form})

def log_in(request):
    template_response = 'doctors/login.html'
    if request.method=='POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('index_pacients'))
            pass
        else:
            print "Ya valio"
            messages.error(request, u'Usuario/Password incorrecto')
            return render(request, template_response, {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, template_response, {'form': form})

def log_out(request):
    logout(request)
    return redirect(reverse('login'))