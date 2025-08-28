from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('solicitud/', views.solicitud, name='solicitud'),
    path('calificacion/', views.calificacion, name='calificacion'),
    path('respuesta/', views.respuesta, name='respuesta'),
]
