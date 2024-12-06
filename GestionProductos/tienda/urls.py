from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, OrdenViewSet

router = DefaultRouter()
router.register('productos', ProductoViewSet)
router.register('ordenes', OrdenViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
from django.urls import path
from . import views

urlpatterns += [
    path('productos/', views.listar_productos, name='listar_productos'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]
