from django.db import models
import uuid #creates unique istance for the event prenotation
from django.contrib.auth.models import User
from datetime import date

# Django rest authentication includes

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# List Import

from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import ArrayField

class Event(models.Model):
    name = models.CharField(max_length=200, default='name')

    subsStart = models.CharField(max_length=200, default='subsStart')
    contDeadline = models.CharField(max_length=200, default='contDeadline')
    subsDeadline = models.CharField(max_length=200, default='subsDeadline')
    nation = models.CharField(max_length=200, default='nation')
    city = models.CharField(max_length=200, default='city')
    address = models.CharField(max_length=200, default='address')
    cap = models.CharField(max_length=200, default='cap')
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
    event = models.IntegerField(default=0)
    user = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)

class Document(models.Model):
    name = models.CharField(max_length=255)
    document = models.FileField(upload_to='reservations/static/documents')
    reservation = models.CharField(max_length=200, default='reservation')


# This code is triggered whenever a new user has been created and saved to the database

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
