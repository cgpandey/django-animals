# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User

animal_type = (('Dogs', 'Dogs'), ('Cats', 'Cats'))

class Animals(models.Model):
	owner = models.ForeignKey(User)
	animal_type = models.CharField(max_length=20, choices=animal_type)
	name = models.CharField(max_length=100)
	birthday = models.DateField()