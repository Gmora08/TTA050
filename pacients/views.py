from django.shortcuts import render
from doctors.models   import Doctor
from pacients.models  import Pacient

def show(request):
    print request.user
    template_response = 'pacients/show.html'
    pacients = Pacient.objects.all()
    return render(request, template_response, {'pacients': pacients})
