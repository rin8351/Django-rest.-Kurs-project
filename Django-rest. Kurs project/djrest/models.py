from enum import auto
from django.db import models
from django.urls import reverse
import requests
import xml.etree.ElementTree as ET
import datetime
from django.contrib.auth.models import User

class valute(models.Model):
    date = models.DateField()
    krs = models.DecimalField(max_digits=10, decimal_places=4)

class kurs(models.Model):
    order = models.IntegerField()
    price_dol = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    price_rub = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)


    def __str__(self):
        return str(self.order)

    def get_absolute_url(self):
        return reverse('kurs')


    def save(self, *args, **kwargs):
        kurs_d = valute.objects.all()
        d = self.date
        new_kurs = valute.objects.get(date=d).krs
        self.price_rub = self.price_dol * new_kurs
        super(kurs,self).save(*args, **kwargs)

    def get_root(self,d):
        d_url = d.strftime("%d/%m/%Y")
        url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='+d_url
        response = requests.get(url)
        root = ET.fromstring(response.content)
        return root

    def dobavlenie_kursa(self,root):
        if root.findall('Valute') == []:
            today = datetime.date.today()
            d = today.strftime("%d/%m/%Y")
            root = self.get_root(d)
        for valute in root.findall('Valute'):
            if valute.get('ID') == 'R01235':
                new_kurs = valute.find('Value').text
        return new_kurs