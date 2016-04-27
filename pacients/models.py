from __future__ import unicode_literals

from django.db import models

class Pacient(models.Model):
    name = models.CharField("Nombre", max_length=30)
    last_name = models.CharField("Apellido", max_length=30)
    date_of_birth = models.DateField("Fecha de nacimento")
    email = models.EmailField()
    SEX_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    sex = models.CharField("Sexo", max_length=1, choices=SEX_CHOICES)
    curp = models.CharField("CURP", max_length=20, default=None)
    BLOOD_CHOICES = (
        ('O+',  'O+'),
        ('O-',  'O-'),
        ('A+',  'A+'),
        ('A-',  'A-'),
        ('B+',  'B+'),
        ('B-',  'B-'),
        ('AB-', 'AB-'),
        ('AB+', 'AB+'),
    )
    blood = models.CharField("Tipo de sangre", max_length=4, choices=BLOOD_CHOICES, default=None)
    phone_number = models.CharField("Numero de telefono", max_length=12, blank=True, null=True)
    address = models.CharField("Direccion", max_length=100, blank=True, null=True)
    cp = models.IntegerField("Codigo Postal", blank=True, null=True)
    state = models.CharField("Estado", max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.name 
