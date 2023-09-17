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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text':''}
        widgets = {'body': forms.Textarea(attrs = {'cols': 40})}
        
class PollForm(forms.Form):
    question = forms.CharField(max_length=100)
    choices = forms.CharField(max_length=500, initial="Each choice should go on a different line.",
                              widget=forms.Textarea(attrs={'cols':40}))
    