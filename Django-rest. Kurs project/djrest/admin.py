from django.contrib import admin
from .models import *

class kursadmin(admin.ModelAdmin):
    list_display= ('order', 'price_dol', 'date')

admin.site.register(valute)
admin.site.register(kurs, kursadmin)