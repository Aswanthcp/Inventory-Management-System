from rest_framework import generics
from .serializers import SuppliersSerializers
from .models import SupplierModels


class SuppliersListCreate(generics.ListCreateAPIView):
    queryset = SupplierModels.objects.all()
    serializer_class = SuppliersSerializers


class SuppliersDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupplierModels.objects.all()
    serializer_class = SuppliersSerializers
    lookup_field = "id"
