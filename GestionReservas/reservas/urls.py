from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehiculoViewSet, ReservaViewSet

router = DefaultRouter()
router.register('vehiculos', VehiculoViewSet)
router.register('reservas', ReservaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
urlpatterns += [
    path('verificar_disponibilidad/<int:vehiculo_id>/<str:fecha_inicio>/<str:fecha_fin>/', verificar_disponibilidad),
    path('', listar_vehiculos, name='listar_vehiculos'),
    path('<int:vehiculo_id>/', detalle_vehiculo, name='detalle_vehiculo'),
    path('mis_reservas/', ver_reservas, name='ver_reservas'),
]
