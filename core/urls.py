from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('solicitud/', views.solicitud, name='solicitud'),
    path('calificacion/<int:pk>/', views.calificacion, name='calificacion'),
    path('respuesta/<int:pk>/', views.respuesta, name='respuesta'),
    path('resumen/', views.resumen, name='resumen'),
    path('solicitudes/', views.solicitudes, name='solicitudes'),
    
]
