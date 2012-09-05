from django import forms
from django.forms.widgets import RadioSelect, Textarea

class TempUserForm(forms.Form):
    duration = forms.IntegerField(
        label='Varighet',
        required=True,
        initial=1,
        min_value=1,
        max_value=120) # 4 months
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
