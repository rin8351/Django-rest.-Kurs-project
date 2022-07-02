from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm

class DateInput(forms.DateInput):
    input_type = 'date'

class AddkursForm(forms.ModelForm):
    class Meta:
        model= kurs
        fields = ['number', 'price_dol', 'date']
        widgets = {
            'date': DateInput(format='%Y-%m-%d'),
        }

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', max_length=30, widget = forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
