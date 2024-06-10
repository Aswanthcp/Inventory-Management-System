from rest_framework import serializers
from .models import Product
from category.serializers import CategorySerializers
from supplier.serializers import SuppliersSerializers
from supplier.serializers import SuppliersSerializers
from warehouse.serializers import WarehouseSerializers

from category.models import CategoryModels
from supplier.models import SupplierModels
from warehouse.models import WarehouseModels


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializers(read_only=True)
    supplier = SuppliersSerializers(read_only=True)
    warehouse = WarehouseSerializers(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "category",
            "supplier",
            "warehouse",
            "quantity",
            "price",
            "low_stock_threshold",
        ]
