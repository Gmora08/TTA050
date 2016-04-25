# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-12 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacients', '0002_auto_20160412_1700'),
        ('doctors', '0002_doctor_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_image', models.URLField(null=True)),
                ('second_image', models.URLField(null=True)),
                ('route_report', models.URLField(null=True)),
                ('linfocitos', models.IntegerField(null=True)),
                ('basofilos', models.IntegerField(null=True)),
                ('monocito', models.IntegerField(null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.Doctor')),
                ('pacient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pacients.Pacient')),
            ],
        ),
    ]
