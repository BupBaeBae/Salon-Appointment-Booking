
from django import forms
from .models import Guest, Slot

class BookingForm(forms.Form):
    name = forms.CharField(max_length=100)
    slot = forms.ModelChoiceField(queryset=Slot.objects.filter(is_open=True))

class CancelForm(forms.Form):
    key = forms.CharField(max_length=20)
