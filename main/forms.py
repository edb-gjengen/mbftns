from django import forms
from django.forms.widgets import RadioSelect, Textarea

class TempUserForm(forms.Form):
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
    description = forms.CharField(
        label='Hvem og hvorfor',
        widget=Textarea,
        max_length=255,
        required=True)
    count = forms.IntegerField(
        label='Hvor mange',
        initial=1,
        required=True,
        min_value=1,
        max_value=30)
