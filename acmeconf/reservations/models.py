from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    seats = models.IntegerField(default=0)
    date = models.DateTimeField('date published')

class EventFee(models.Model):
    event = models.ForeignKey(Event, related_name='fee_options', on_delete=models.DO_NOTHING)
    available = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=255,decimal_places=2)

class EventChoice(models.Model):
    event = models.ForeignKey(Event, related_name='choices', on_delete=models.DO_NOTHING)
    order = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=32)
    label = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    required = models.BooleanField(default=False)
    allow_multiple = models.BooleanField(default=False)
