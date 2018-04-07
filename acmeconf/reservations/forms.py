from django.contrib.auth.models import User
from django import forms
from .models import EventReservation
from .models import Event

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        exclude = ()

class EventReservationForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100)
    password = forms.CharField(label='Password', max_length=100)

    class Meta:
        model = EventReservation
        fields = ['event']
        exclude = ()
