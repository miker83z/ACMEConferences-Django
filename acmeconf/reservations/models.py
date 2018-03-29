from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    seats = models.IntegerField(default=0)
    date = models.DateTimeField('date published')
    
