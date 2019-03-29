from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404


from .models import Producto
from .serializers import ProductoSerializer, UserSerializer


class ProductoList(APIView):
    def get(self, request):
        prod = Producto.objects.all()
        data = ProductoSerializer(prod, many=True).data
        return Response(data)


class ProductoDetalle(APIView):
    def get(self, request, pk):
        prod = get_object_or_404(Producto, pk=pk)
        data = ProductoSerializer(prod, many=False).data
        return Response(data)


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer
