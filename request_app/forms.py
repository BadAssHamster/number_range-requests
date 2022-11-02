from django import forms
from .models import Requests


class RequestForm(forms.ModelForm):
    class Meta:
        model = Requests
        fields = ['doc_type', 'count']


class MoAlterForm(forms.ModelForm):
    class Meta:
        model = Requests
        fields = ['doc_type', 'count']


class MiacSubmitForm(forms.ModelForm):
    class Meta:
        model = Requests
        fields = ['numbers']
