from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from .models import Event

def index(request):
    latest_event_list = Event.objects.order_by('-date')[:5]
    template = loader.get_template('reservations/index.html')
    context = {
        'latest_event_list': latest_event_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, event_id):
    return HttpResponse("You're looking at event %s." % event_id)
