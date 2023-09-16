from django import forms

from .models import *

class PollForm(forms.Form):
    choice = forms.ChoiceField(choices=())