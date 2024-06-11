from rest_framework import generics
from .serializers import WarehouseSerializers
from .models import WarehouseModels
from products.serializers import ProductSerializer
from products.models import Product
from rest_framework.permissions import IsAuthenticated


class WarehouseListCreate(generics.ListCreateAPIView):
    queryset = WarehouseModels.objects.all()
    serializer_class = WarehouseSerializers
    permission_classes = [IsAuthenticated]


class WarehouseDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = WarehouseModels.objects.all()
    serializer_class = WarehouseSerializers
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


class WarehouseProductsList(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        warehouse_id = self.kwargs["id"]
        return Product.objects.filter(warehouse=warehouse_id)
