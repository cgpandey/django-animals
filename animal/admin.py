# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Animals
class AnimalAdmin(admin.ModelAdmin):
      list_display = ('name','animal_type','birthday')
      search_fields = ('name','animal_type','birthday')
      list_per_page = 50 # No of records per page

admin.site.register(Animals,AnimalAdmin)