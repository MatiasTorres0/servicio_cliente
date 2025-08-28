from django.shortcuts import render, redirect
from .forms import SolicitudForm, CalificacionForm, RespuestaForm

# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')
def solicitud(request):
    if request.method == 'POST':
        form = S(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:enviado')
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