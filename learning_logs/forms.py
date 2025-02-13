from django import forms
from .models import Topic, Entry


class TopicForms(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'ex_data']
        labels = {'text': 'Entry:', 'ex_data': 'Your image:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}