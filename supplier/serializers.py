from rest_framework import serializers
from .models import SupplierModels


class SuppliersSerializers(serializers.ModelSerializer):
    class Meta:
        model = SupplierModels
        fields = "__all__"
