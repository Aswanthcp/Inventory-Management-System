from rest_framework import serializers
from .models import WarehouseModels


class WarehouseSerializers(serializers.ModelSerializer):
    class Meta:
        model = WarehouseModels
        fields = "__all__"
