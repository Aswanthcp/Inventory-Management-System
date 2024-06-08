from rest_framework import generics
from .serializers import WarehouseSerializers
from .models import WarehouseModels


class WarehouseListCreate(generics.ListCreateAPIView):
    queryset = WarehouseModels.objects.all()
    serializer_class = WarehouseSerializers


class WarehouseDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = WarehouseModels.objects.all()
    serializer_class = WarehouseSerializers
    lookup_field = "id"
