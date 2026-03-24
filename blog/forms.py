from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """
    Collects one instance of :model:`blog.Comment`
    
    """
    class Meta:
        model = Comment
        fields = ('body',)