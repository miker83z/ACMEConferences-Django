from django.urls import path
from . import views
from django.conf.urls import url
import booking


app_name = 'reservations'

urlpatterns = [
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^(?P<event_id>[0-9]+)/booking/$', views.reservation, name='reservation'),
    url(r'^$', views.index, name='index'),
    path('<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
]
