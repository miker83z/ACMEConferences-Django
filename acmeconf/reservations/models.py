from django.db import models
import uuid #creates unique istance for the event prenotation
from django.contrib.auth.models import User
from datetime import date


class Event(models.Model):
    name = models.CharField(max_length=200, default='name')
    location = models.CharField(max_length=200, default='location')
    max_seats = models.IntegerField(default=0)
    available_seats = models.IntegerField(default=0)
    date = models.DateTimeField('date published', auto_now=True)
    ticket_price = models.IntegerField(default=0)
    staff_ticket_price = models.IntegerField(default=0)
    available_money = models.IntegerField(default=0)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class EventReservation(models.Model):
    event = models.CharField(max_length=200, default='event')
    user = models.CharField(max_length=200, default='name')
