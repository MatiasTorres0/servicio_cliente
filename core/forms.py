from django import forms
from . import models

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = models.servicio_cliente
        fields = [
            'tipo_problema',
            'descripcion',
        ]

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = models.servicio_cliente
        fields = [
            'fecha_respuesta',
            'respuesta',
            'estado',
            'solucion',
            'fecha_solucion',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['respuesta'].widget.attrs.update({'rows': 4})
        self.fields['solucion'].widget.attrs.update({'rows': 4})



class CalificacionForm(forms.ModelForm):
    class Meta:
        model = models.servicio_cliente
        fields = [
            'calificacion',
            'comentario',
            'fecha_comentario',
        ]
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 4}),
            'calificacion': forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs.update({'class': 'form-control'})