from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, null=True)
    email = models.EmailField(unique=True)
    SEX = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    first_name = models.CharField("Nombre", max_length=30)
    last_name = models.CharField("Apellidos", max_length=30)
    date_of_birth = models.DateField("Fecha de nacimiento")
    sex = models.CharField("Sexo", choices=SEX, max_length=1)

    def __unicode__(self):
        return self.email

