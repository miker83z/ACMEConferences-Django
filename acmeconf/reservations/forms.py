from django.contrib.auth.models import User
from django import forms
from .models import EventReservation
from .models import Event

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff']
        exclude = ()
        labels = {
            'is_staff': ('Conference Speaker'),
        }
        help_texts = {
            'username': None,
            'is_staff': ('Check it if you are a conference speaker'),
        }

class EventReservationForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100)
    password = forms.CharField(label='Password', max_length=100)

    class Meta:
        model = EventReservation
        fields = ['event']
        exclude = ('event',)
