from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'reservations'

urlpatterns = [
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    path('', views.index, name='index'),
    path('<int:event_id>/', views.detail, name='detail'),
]
