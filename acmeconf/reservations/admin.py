from django.contrib import admin

from .models import Event
from .models import EventReservation

admin.site.register(Event)
admin.site.register(EventReservation)
