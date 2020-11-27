from django.forms import ModelForm,CharField
from .models import Comment


class CommentForm(ModelForm):
    text=CharField(max_length=200,label="Comment")
    class Meta:
        model = Comment
        fields = ['text']
