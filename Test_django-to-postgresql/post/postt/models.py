from django.db import models
from django.urls import reverse
from django.core.files import File
import requests
import xml.etree.ElementTree as ET
import datetime


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
    # Сначала считывается текстовый файл с курсами валют
    def save(self, *args, **kwargs):
        kurs_d = {}
        with open('k.txt', 'r') as f:
            myfile = File(f)
            for line in myfile:
                key, value = line.split()
                kurs_d[key] = value
        myfile.close()
        d = self.date.strftime('%d/%m/%Y')
        # Если курса валют нет в текстовом файле, новый 
        # курс берется из базы данных ЦБ
        if d not in kurs_d:
            kurs_d[d] = self.dobavlenie_kursa(self.get_root(d))
        new_kurs=float(kurs_d[d].replace(',', '.'))
        self.price_rub = round(self.price_dol*new_kurs, 2)
        with open('k.txt', 'w') as f:
            for key, value in kurs_d.items():
                f.write(key + ' ' + value + '\n')
        myfile.closed

        super(kurs,self).save(*args, **kwargs)

    def get_root(self,d):
        url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='+d
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
