from django import forms

from .models import *

class PollForm(forms.Form):
    choice = forms.ChoiceField(choices=())
    
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'body']
        labels = {'title':'Title:', 'body':'Text:'}
        widgets = {'body':forms.Textarea(attrs={'cols': 80})}