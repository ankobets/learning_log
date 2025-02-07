from django import forms
from .models import Topic

class TopicForms(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}