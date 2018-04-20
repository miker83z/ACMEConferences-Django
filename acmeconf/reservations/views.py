from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from django.http import HttpResponse
from django.template import loader
from .models import Event
from django.views.generic import DetailView
from .forms import EventReservationForm
from django.contrib.auth.models import User
from zeep import Client
from django.shortcuts import render_to_response


def index(request):
    latest_event_list = Event.objects.order_by('-date')[:5]
    template = loader.get_template('reservations/index.html')
    context = {
        'latest_event_list': latest_event_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, event_id):
    return HttpResponse("You're looking at event %s." % event_id)

class UserFormView(View):
    form_class = UserForm
    template_name = 'reservations/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            #istantiates a user from the form, that is added to the user that we will see in the admin panel
            user = form.save(commit=False)

            #cleaned (normalized) databases
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            #save the user in the database
            user.save()

            #returns User object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('reservation:index')

        return render(request, self.template_name, {'form': form})

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('reservations:index')
    context = {
        "form": form,
    }
    return render(request, 'reservations/register.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('reservations:index')
            else:
                return render(request, 'reservations/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'reservations/login.html', {'error_message': 'Invalid login'})
    return render(request, 'reservations/login.html')

class EventDetailView(generic.DetailView):
    model = Event


def reservation(request, event_id):
    #retrieve an event object by id
    original_event = Event.objects.get(id=event_id)
    if original_event.available_seats > 0 or original_event.is_open == True:
        if request.method == 'POST':
            form = EventReservationForm(request.POST)
            if form.is_valid():
                event = form.save()
                event.user = request.user.id
                event.event = original_event.id
                original_event.available_seats = original_event.available_seats - 1

                original_event.available_money = original_event.available_money + original_event.ticket_price

                #establish the connection to the bank server
                client = Client('http://localhost/Banca/server.wsdl')

                #get bank username and password from the validate form
                name = form.cleaned_data['name']
                password = form.cleaned_data['password']

                #send form data to the bank login service
                risposta = client.service.userLogin(name, password)

                client.service.transferPayment(2.3, 'michele', risposta['userID'])
                client.service.userLogout(risposta['userID'])

                original_event.save()
                event.save()
                return render_to_response('reservations/booked.html')
        else:
            form = EventReservationForm()
        return render(request, 'reservations/reservation.html', {
            'form': form
        })
    else:
        original_event.is_open = False
        original_event.save()
        return render_to_response('reservations/closed.html')

#testing
