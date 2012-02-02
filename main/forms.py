from django import forms
from django.forms.widgets import RadioSelect

class TempUserForm(forms.Form):
    who = forms.CharField(label='Hvem', required=True)
    RANGE_CHOICES = (
        ('1', '1 dag'),
        ('2', '2 dager'),
        ('7', '1 uke (7 dager)'),
    )
    duration = forms.TypedChoiceField(
        label='Varighet',
        coerce=int,
        choices=RANGE_CHOICES,
        widget=RadioSelect,
        required=True)
    why = forms.CharField(label='Hvorfor', required=True)
