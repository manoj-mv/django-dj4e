from django import forms
from .models import Message
class ChatForm(forms.ModelForm):
    text = forms.CharField(max_length=200)
    class Meta:
        model = Message
        fields = ['text']
       