from django.forms import ModelForm

from main.models import *

class TempUserForm(ModelForm):
    # TODO : Move this to radius?
    class Meta:
        model = TempUser 
