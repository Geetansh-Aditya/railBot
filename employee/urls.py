from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/complaints/', views.get_complaint, name='get_complaints'),
]