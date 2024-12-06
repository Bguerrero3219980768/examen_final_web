from rest_framework import viewsets
from .models import Vehiculo, Reserva
from .serializers import VehiculoSerializer, ReservaSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
from django.http import JsonResponse
from django.db.models import Q

def verificar_disponibilidad(request, vehiculo_id, fecha_inicio, fecha_fin):
    reservas = Reserva.objects.filter(
        vehiculo_id=vehiculo_id,
        fecha_fin__gte=fecha_inicio,
        fecha_inicio__lte=fecha_fin,
    )
    disponible = not reservas.exists()
    return JsonResponse({'disponible': disponible})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehiculo, Reserva
from django.contrib.auth.decorators import login_required

def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.filter(disponible=True)
    return render(request, 'reservas/listar_vehiculos.html', {'vehiculos': vehiculos})

def detalle_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    if request.method == 'POST':
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']
        precio = (Vehiculo.objects.get(id=vehiculo_id).precio_dia * (fecha_fin - fecha_inicio).days)
        Reserva.objects.create(usuario=request.user, vehiculo=vehiculo, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, precio=precio)
        return redirect('ver_reservas')
    return render(request, 'reservas/detalle_vehiculo.html', {'vehiculo': vehiculo})

@login_required
def ver_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user)
    return render(request, 'reservas/ver_reservas.html', {'reservas': reservas})
