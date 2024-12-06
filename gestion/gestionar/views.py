from django.shortcuts import render, get_object_or_404, redirect
from .models import Proyecto

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos.html', {'proyectos': proyectos})

def detalle_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    return render(request, 'detalle_proyecto.html', {'proyecto': proyecto})

def nuevo_proyecto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        Proyecto.objects.create(nombre=nombre, descripcion=descripcion)
        return redirect('/')
    return render(request, 'nuevo_proyecto.html')
