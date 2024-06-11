from rest_framework import generics
from .serializers import SuppliersSerializers
from .models import SupplierModels
from products.serializers import ProductSerializer
from products.models import Product
from rest_framework.permissions import IsAuthenticated


class SuppliersListCreate(generics.ListCreateAPIView):
    queryset = SupplierModels.objects.all()
    serializer_class = SuppliersSerializers
    permission_classes = [IsAuthenticated]


class SuppliersDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupplierModels.objects.all()
    serializer_class = SuppliersSerializers
    lookup_field = "id"
    permission_classes = [IsAuthenticated]


class SupplierProductsList(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        supplier_id = self.kwargs["id"]
        return Product.objects.filter(supplier=supplier_id)
