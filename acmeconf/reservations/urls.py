from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'reservations'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.index, name='index'),
    path('<int:event_id>/', views.detail, name='detail'),
]
