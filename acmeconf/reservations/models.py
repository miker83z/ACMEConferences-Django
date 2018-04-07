from django.db import models
import uuid #creates unique istance for the event prenotation
from django.contrib.auth.models import User
from datetime import date


class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    max_seats = models.IntegerField(default=0)
    available_seats = models.IntegerField(default=0)
    date = models.DateTimeField('date published')
    ticket_price = models.IntegerField(default=0)
    available_money = models.IntegerField(default=0)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class EventReservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for the reservation")
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    reservation = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
