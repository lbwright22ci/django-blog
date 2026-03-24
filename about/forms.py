
from django import forms
from .models import CollaborateRequest

class CollaborateForm(forms.ModelForm):
    """
    Creates :form: from the :model:`about.CollaborateRequest`
    Fields collected by the form are 'name', 'email' and 'messsage'
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name','email','message',)