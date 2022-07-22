

from django.urls import path, include
from app_coder.views import familia , lista_familia

urlpatterns = [
    path('agrega-familia/ <nombre>/<edad>/<cumpleaños>/', familia),
    path('lista-familiares/', lista_familia),
]
