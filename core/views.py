from django.shortcuts import render, redirect
from .forms import SolicitudForm, CalificacionForm, RespuestaForm
from .models import servicio_cliente  # Changed to capital letter to match model name convention
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')

@login_required
def solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            # Guardar la solicitud asociándola al usuario actual
            solicitud = form.save(commit=False)
            solicitud.user = request.user  # Asigna el usuario actual
            solicitud.save()
            return redirect('solicitudes')  # Redirige a la lista de solicitudes
    else:
        form = SolicitudForm()
    
    return render(request, 'core/solicitud.html', {'form': form})

def calificacion(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:enviado')
    else:
        form = CalificacionForm()
    return render(request, 'core/calificación.html', {'form': form})

def respuesta(request):
    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:enviado')
    else:
        form = RespuestaForm()
    return render(request, 'core/respuesta.html', {'form': form})

def resumen(request):
    return render(request, 'dashboard/resumen.html')

def solicitudes(request):
    solicitudes = servicio_cliente.objects.all()  # Changed to capital letter to match model name
    return render(request, 'dashboard/solicitudes.html', {'solicitudes': solicitudes})