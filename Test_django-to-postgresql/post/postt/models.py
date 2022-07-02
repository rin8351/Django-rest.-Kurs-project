from enum import auto
from django.db import models
from django.urls import reverse
import requests
import xml.etree.ElementTree as ET
import datetime


class valute(models.Model):
    date = models.DateField()
    krs = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('valute')

class kurs(models.Model):
    number = models.IntegerField()
    price_dol = models.IntegerField()
    date = models.DateField()
    price_rub = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return str(self.number)

    def get_absolute_url(self):
        return reverse('kurs')

    # Функция записи рублевой стоимости в базу данных
    def save(self, *args, **kwargs):
        kurs_d = valute.objects.all()
        d = self.date
        # Если курса валют на нужную дату нет - 
        # берем его из базы данных ЦБРФ
        if d not in [k.date for k in kurs_d]:
            root = self.get_root(d)
            new_kurs = self.dobavlenie_kursa(root)
            new_kurs = float(new_kurs.replace(',', '.'))
            valute.objects.create(date=d, krs=new_kurs)
        else:
            new_kurs = valute.objects.get(date=d).krs
        self.price_rub = round(self.price_dol*new_kurs, 2)
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
