from __future__ import unicode_literals

from django.db import models
from doctors.models import Doctor
from pacients.models import Pacient

class Report(models.Model):
    doctor       = models.ForeignKey(Doctor)
    pacient      = models.ForeignKey(Pacient)
    image        = models.ImageField(upload_to='img/', default='img/test/img1.jpg')
    second_image = models.URLField(max_length=200, null=True, blank=True)
    route_report = models.URLField(max_length=200, null=True, blank=True)
    linfocitos   = models.IntegerField(null=True) 
    basofilos    = models.IntegerField(null=True)
    created_at   = models.DateTimeField(auto_now_add=True, editable=False)