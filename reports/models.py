from __future__ import unicode_literals

from django.db import models
from doctors.models import Doctor
from pacients.models import Pacient

class Report(models.Model):
    doctor       = models.ForeignKey(Doctor)
    pacient      = models.OneToOneField(Pacient)
    first_image  = models.URLField(max_length=200, null=True)
    second_image = models.URLField(max_length=200, null=True)
    route_report = models.URLField(max_length=200, null=True)
    linfocitos   = models.IntegerField(null=True) 
    basofilos    = models.IntegerField(null=True)
    monocito     = models.IntegerField(null=True)
