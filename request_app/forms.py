from django import forms
from .models import Requests


status_choice = (
    (1, 'Черновик'),
    (2, 'Отправлена'),
    (3, 'Выполнена')
)


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
