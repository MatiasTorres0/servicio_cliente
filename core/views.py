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
@login_required
def calificacion(request, pk):
    instancia = servicio_cliente.objects.get(id=pk, user=request.user)  # Asegura que pertenezca al usuario
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('solicitudes')  # O a donde quieras redirigir
    else:
        form = CalificacionForm(instance=instancia)
    return render(request, 'core/calificación.html', {'form': form})

@login_required
def respuesta(request, pk):
    instancia = servicio_cliente.objects.get(id=pk)  # Puedes agregar filtros si es necesario
    if request.method == 'POST':
        form = RespuestaForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('solicitudes')
    else:
        form = RespuestaForm(instance=instancia)
    return render(request, 'core/respuesta.html', {'form': form})
@login_required
def resumen(request):
    return render(request, 'dashboard/resumen.html')
@login_required
def solicitudes(request):
    solicitudes = servicio_cliente.objects.all()  # Changed to capital letter to match model name
    return render(request, 'dashboard/solicitudes.html', {'solicitudes': solicitudes})