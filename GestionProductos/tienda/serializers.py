from rest_framework import serializers
from .models import Producto, Orden, OrdenProducto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class OrdenSerializer(serializers.ModelSerializer):
    productos = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all(), many=True)

    class Meta:
        model = Orden
        fields = ['id', 'usuario', 'fecha', 'total', 'productos']
