from django import forms

#from radius.models import *
#
#class TempUserForm(forms.ModelForm):
#    # TODO : Move this to radius?
#    class Meta:
#        model = TempUser 
class TempUserForm(forms.Form):
    who = forms.CharField(label='Hvem')
    RANGE_CHOICES = (
        ('1 day', '1 dag'),
        ('2 days', '2 dager'),
        ('7 days', '1 uke (7 dager)'),
    )
    duration = forms.ChoiceField(label='Varighet', choices=RANGE_CHOICES)
    why = forms.CharField(label='Hvorfor')
