from django.db import models

# Create your models here.
class servicio_cliente(models.Model):
    TIPO_PROBLEMA = (
        ('1', 'Problema con la cuenta'),
        ('2', 'Problema con el canal'),
        ('3', 'Problema con el juego'),
        ('4', 'Problema con un bot del chat'),
        ('5', 'Otro'),
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tipo_problema = models.CharField(max_length=1, choices=TIPO_PROBLEMA, default='1')
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1, choices=(('1', 'Activo'), ('2', 'Cerrado')), default='1')
    respuesta = models.TextField(blank=True, null=True)
    fecha_respuesta = models.DateTimeField(blank=True, null=True)
    solucion = models.TextField(blank=True, null=True)
    fecha_solucion = models.DateTimeField(blank=True, null=True)
    calificacion = models.CharField(max_length=1, choices=(
        ('1', '★'),
        ('2', '★★'), 
        ('3', '★★★'),
        ('4', '★★★★'),
        ('5', '★★★★★')
    ), blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)
    fecha_comentario = models.DateTimeField(blank=True, null=True)

