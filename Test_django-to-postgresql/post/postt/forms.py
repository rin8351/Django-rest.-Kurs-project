from django import forms
from .models import *

class AddkursForm(forms.ModelForm):
    class Meta:
        model= kurs
        fields = ['number', 'price_dol', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
        }
