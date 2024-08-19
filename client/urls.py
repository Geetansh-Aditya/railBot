from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
    path('', views.general_info, name='general_info'),
    path('send_message/', views.send_message, name='send_message'),
    path('sahayak/', views.index, name='index'),
]