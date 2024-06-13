from django.urls import path
from proyectowebapp import views

urlpatterns = [
    path('', views.home, name='home')
]
