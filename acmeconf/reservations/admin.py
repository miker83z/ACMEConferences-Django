from django.contrib import admin

from .models import Event
from .models import EventReservation
from .models import Document

admin.site.register(Event)
admin.site.register(EventReservation)
admin.site.register(Document)
